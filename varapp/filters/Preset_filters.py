"""
Preset configurations.
"""

from varapp.filters import filters_factory as ffac


FOR_ANY_COMMON_VARS = [('pass_filter', '=', 'PASS'),
                     ('aaf_1kg_all', '<=', 0.01),
                     ('aaf_exac_all', '<=', 0.01),
                     ('aaf_esp_all', '<=', 0.01),
                     ('in_dbsnp','=','true')]

gene_func_filters = [('is_splicing','=','true')]


exon_func_filters_rank1 = [('impact', '=', ','.join(
                            ['frameshift_variant',
                             'stop_gained',
                             'stop_lost',
                             'non_synoymous_start',
                             'missense_variant',
                             'inframe_deletion',
                            'inframe_insertion'])
                            )]

exon_func_filters_rank2 = [('impact', '=', ','.join(
                            ['frameshift_variant',
                             'stop_gained',
                             'stop_lost'])
                            )]
PATHOGENIC_CONFIG = [('clinvar_sig','=','pathogenic')]

def Preset1ForFinal(name, op, val, db=None, samples_selection=None):
    filters_config = FOR_ANY_COMMON_VARS + gene_func_filters + exon_func_filters_rank1


    f_collection=[]
    for i,k,v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection


def Preset2ForImportant(name, op, val, db=None, samples_selection=None):
    filters_config = FOR_ANY_COMMON_VARS + exon_func_filters_rank2
    f_collection=[]
    for i,k,v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection

def Preset3ForPathogenic(name, op, val, db=None, samples_selection=None):
    filters_config = FOR_ANY_COMMON_VARS + PATHOGENIC_CONFIG
    f_collection=[]
    for i,k,v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection








