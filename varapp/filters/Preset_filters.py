"""
Preset configurations.
"""

from varapp.filters import filters_factory as ffac

FOR_ANY_COMMON_VARS = [('pass_filter', '=', 'PASS'),
                       ('aaf_1kg_all', '<=', 0.01),
                       ('aaf_exac_all', '<=', 0.01),
                       ('aaf_esp_all', '<=', 0.01)
                       ]

GENE_FUNC_FILTERS = [('is_splicing', '=', 'true')]

EXON_FUNC_FILTERS_RANK1 = [('impact', '=', ','.join(
    ['frameshift',
     'frameshift_variant',
     'stop_gained',
     'stop_lost',
     'non_synoymous_start',
     'missense_variant',
     'inframe_deletion',
     'inframe_insertion'])
                            )]

EXON_FUNC_FILTERS_RANK2 = [('impact', '=', ','.join(
    ['frameshift',
     'frameshift_variant',
     'stop_gained',
     'stop_lost'])
                            )]

PATHOGENIC_CONFIG = [('clinvar_sig', '=', 'pathogenic')]


def Preset1ForFinal(db=None):
    filters_config = FOR_ANY_COMMON_VARS + EXON_FUNC_FILTERS_RANK1

    f_collection = []
    for i, k, v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection


def Preset1b_ForFinal(db=None):
    filters_config = FOR_ANY_COMMON_VARS + GENE_FUNC_FILTERS

    f_collection = []
    for i, k, v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection


def Preset2ForImportant(db=None):
    filters_config = FOR_ANY_COMMON_VARS + EXON_FUNC_FILTERS_RANK2
    f_collection = []
    for i, k, v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection


def Preset3ForPathogenic(db=None):
    filters_config = FOR_ANY_COMMON_VARS + PATHOGENIC_CONFIG
    f_collection = []
    for i, k, v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection
