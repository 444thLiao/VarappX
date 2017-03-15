import csv, datetime
from varapp.models.gemini import Samples, Variants
from varapp.common.gemini import *
from varapp.data_models.variants import expose_variant_full, expose_variant, annotate_variants
from varapp.filters.filters_factory import preset_filters_map

import re


def capitalize(x):
    return '' if len(x) == 0 else x[0].upper() + x[1:]


# Transform data keys into header names
COL_NAMES = {
    'genotypes_index': 'Genotypes',
    'rs_ids': 'dbSNP',
    'entrez_gene_id': 'Gene_Entrez',
    'ensembl_gene_id': 'Gene_Ensembl',
    'ensembl_transcript_id': 'Transcript_Ensembl',
    'hgvsc': 'HGVSc',
    'hgvsp': 'HGVSp',
    'aaf_1kg_all': '1KG_freq',
    'aaf_esp_all': 'ESP_freq',
    'aaf_exac_all': 'EXAC_freq',
    'qual_depth': 'Qual_by_depth',
    'strand_bias': 'Strand_bias_Fisher',
    'strand_bias_odds_ratio': 'Strand_bias_SOR',
    'rms_map_qual': 'RMS_map_qual',
    'map_qual_rank_sum': 'Map_qual_rank_sum',
    'cadd_raw': 'CADD_score_raw',
    'cadd_scaled': 'CADD_score_scaled',
    'gerp_bp_score': 'GERP_score',
    'gerp_element_pval': 'GERP_pvalue',
    'read_depth': 'Read_depth',
}

EXCEPT_FIELDS = {'position', }
# EXCEPT_FIELDS = {}

### Help to reconstract some field.
SPECIAL_P_FIELDS = {'allele_freq_raws': 0, 'allele_freq': 0, 'allele_depths_raws': 1, 'allele_depths': 1}





### Export types

def export_report(variants, target, db, params):
    """Generate a report indicating how the variants were called, filtered, and annotated.
    :param params: a dict looking like Request.GET:
        `{'filter':['impact=intron',...], 'samples':['affected=...','not_affected=...']}`
    """
    now = datetime.datetime.now()
    timestamp = now.strftime('%d/%m/%Y %H:%M:%S %p')
    lines = ["VarappX report " + timestamp]
    # Stats on filtered variants
    lines.append("\nReturned {} variants out of {}.".format(len(variants), Variants.objects.using(db).count()))
    # Read GET params and prettify
    lines.append("\nFiltering parameters:")
    lines.append("---------------------")
    storge_filters_config = {}
    for x in params.get('filter', []):
        key, op, val = re.match(r"(\S+?)([<>=]{1,2})(.+)", x).groups()
        storge_filters_config[key] = [key, op, val]
    if 'genotype' in storge_filters_config:
        if not 'none' in storge_filters_config['genotype']:
            filters_config = preset_filters_map[val](db=db)[1]
        else:
            filters_config = [storge_filters_config['genotype']]
        lines.append("FiltersPanel: {}".format(val))
        for key, op, val in filters_config:
            lines.append(" " * 8 + "{} {} {}".format(key, op, val))
        storge_filters_config.pop('genotype')
        lines.append("")
    for f_key in storge_filters_config:
        lines.append("Manual Filter selections:")
        key, op, val = storge_filters_config[f_key]
        lines.append(" " * 8 + "{} {} {}".format(COL_NAMES.get(key, key), op, val))

    lines.append("\nSamples selection:", )
    lines.append("------------------")
    lines.append('\t'.join(['Family', 'Name', 'Father', 'Mother', 'Sex', 'Phenotype']))
    slist = []
    for x in params.get('samples', []):
        group, s = x.split('=')
        slist.extend(s.split(','))
    samples = Samples.objects.using(db).filter(name__in=slist).order_by('phenotype', 'name')
    for s in samples:
        lines.append('\t'.join([s.family_id, s.name, s.paternal_id, s.maternal_id,
                                'male' if s.sex == '1' else 'female',
                                'affected' if s.phenotype == '2' else 'unaffected']))
    # Fetch info from Gemini's vcf_header table
    gemini_version = get_gemini_version(db)
    vcf_header = fetch_vcf_header(db)
    with open('/home/liaoth/Desktop/vcf_header', 'w') as f1:
        f1.write(str(vcf_header))
    # print(vcf_header)
    gatk_version = get_gatk_version(vcf_header)
    vep_version, vep_resources = get_vep_info(vcf_header)
    lines.extend([
        "\nVariant calling method:",
        "-----------------------",
        "GATK {}".format(gatk_version),
        "\nAnnotation:",
        "-----------",
        "Gemini {}".format(gemini_version),
        "VEP {}:".format(vep_version),
    ])
    for k, v in sorted(vep_resources.items(), key=lambda z: z[0].lower()):
        lines.append("    {}: {}".format(k, v))
    # Fetch info from Gemini's resources table
    lines.append("Gemini resources:")
    gemini_resources = fetch_resources(db)
    for k, v in sorted(gemini_resources):
        lines.append("    {}: {}".format(k, v))
    # Write
    for l in lines:
        target.write(l + '\n')


def export_tsv(variants, target, samples_selection, fields):
    """Write the selected fields of each variants on a line, with a header.
    :param target: a writable object - an HTTPResponse in our case.
    :param fields: list of field names (from Variant data model).
    """
    for f in EXCEPT_FIELDS:
        if f in fields:
            fields.remove(f)
    sample_names = [s.name for s in samples_selection if s.active]
    writer = csv.writer(target, delimiter='\t')

    gts_map = {(0, 0): '0/0', (1, 0): '1/0', (0, 1): '0/1', (1, 1): '1/1', (None, None): './.'}
    db = variants.db
    exp = [expose_variant_full(v, samples_selection) for v in variants]
    exp = annotate_variants(exp, db)
    if set(fields).intersection(set(SPECIAL_P_FIELDS.keys())) == set():
        writer.writerow([COL_NAMES.get(f, capitalize(f)) for f in fields])
    else:
        # Make some fields in SPECIAL_P_FIELDS into two columns, normal tumor ordered list.
        list_inters = list(set(fields).intersection(set(SPECIAL_P_FIELDS.keys())))
        for v in exp:
            if v[list_inters[0]] != 'nan':
                if v[list_inters[0]].count(',') > SPECIAL_P_FIELDS[list_inters[0]]:
                    PoS = 'PAIR'
                else:
                    PoS = 'SINGLE'
                break
            else:
                continue
        if PoS == 'PAIR':
            for s_field in list_inters:
                idx = fields.index(s_field)
                fields.insert(idx,s_field+'_Tumor')
                fields.insert(idx, s_field + '_Normal')
                fields.remove(s_field)
        else:
            pass
        writer.writerow([COL_NAMES.get(f, capitalize(f)) for f in fields])
    for v in exp:
        info = []
        except_field=[]
        for field in fields:
            if PoS == 'PAIR' and (field.replace('_Tumor','') in SPECIAL_P_FIELDS or field.replace('_Normal','') in SPECIAL_P_FIELDS):
                field = field.replace('_Tumor','')
                field = field.replace('_Normal','')
                val = v[field].split(',')
                if len(val) == 2 and field not in except_field:
                    info+=val
                elif len(val) == 4 and field not in except_field:
                    info.append(','.join(val[:2]))
                    info.append(','.join(val[2:]))
                else:
                    continue
                except_field.append(field)
                continue

            if field not in v:
                continue
            else:
                val = v[field]
            if field == 'genotypes_index':
                assert len(sample_names) == len(val), "{} samples but {} genotypes".format(len(sample_names), len(val))
                couples = ['{}:{}'.format(s, gts_map[tuple(g)]) for s, g in zip(sample_names, val)]
                info.append(','.join(c for c in couples))
            elif isinstance(val, (list, tuple)):
                info.append(','.join(val))
            else:
                info.append(val)

        writer.writerow(info)


def export_vcf(variants, target, samples_selection):
    """Write all selected variants in VCF format.
    :param target: a writable object - an HTTPResponse in our case.
    """
    sample_names = [s.name for s in samples_selection if s.active]
    vcf_header = fetch_vcf_header(variants.db)
    for h in vcf_header[:-1]:  # last one has the header
        if not h.startswith('##INFO') or h.startswith('##GATKCommandLine') or h.startswith('VEP'):
            target.write(h + '\n')
    # Write the header, which should be the same as in the VCF, but it is safer to force
    # the ordering of the samples to be the same as the genotypes'.
    writer = csv.writer(target, delimiter='\t', lineterminator='\n')
    fields = ['chrom', 'start', 'dbsnp', 'ref', 'alt', 'quality', 'pass_filter']
    header = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'] + [s.upper() for s in
                                                                                            sample_names]
    FORMAT = ['AD','AF']
    writer.writerow(header)
    gts_map = {(0, 0): '0/0', (1, 0): '1/0', (0, 1): '0/1', (1, 1): '1/1', (None, None): './.'}
    for v in variants:
        v = expose_variant(v)
        print(v)
        v['dbsnp'] = ','.join(v['dbsnp'])
        info = []
        for f in fields:
            if f == 'quality' and v[f] == None:
                info.append('.')
            elif f == 'start':
                info.append(v[f] + 1)  ###Turn it into 1-coordinate
            else:
                info.append(v[f])

        info += ['', 'GT'] + [gts_map[tuple(g)] for g in samples_selection.select_x_active(v['genotypes_index'])]
        writer.writerow(info)
