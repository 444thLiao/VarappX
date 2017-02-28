"""
Preset configurations.
"""
from varapp.filters.filters_factory import *



def Preset1ForFinal(name, op, val, db=None, samples_selection=None):
    filters_config= [('pass_filter', '=', 'PASS'),
                     ('aaf_1kg_all', '<=', 0.01),
                     ('aaf_exac_all', '<=', 0.01),
                     ('aaf_esp_all', '<=', 0.01),
                     ('in_dbsnp','=','true')
                      ]

    return filters_config

def Preset2ForImportant(name, op, val, db=None, samples_selection=None):
    filters_config=(('pass_filter','=','PASS'),
                  ('aaf_1kg_all','<=',0.01),
                  ('aaf_exac_all','<=',0.01),
                  ('aaf_esp_all','<=',0.01)
                   )

    return filters_config

def Preset3ForPathogenic(name, op, val, db=None, samples_selection=None):
    filters_config=(('pass_filter','=','PASS'),
                  ('aaf_1kg_all','<=',0.01),
                  ('aaf_exac_all','<=',0.01),
                  ('aaf_esp_all','<=',0.01))
    return filters_config

def snp138Common_filters():
    snp138_common_file='/home/liaoth/data/humandb/snp138Common.name.txt'
    lines = open(snp138_common_file,'r').readlines()
    lines = [it.strip() for it in lines]
    snp138_common = list(set(lines))
    return snp138_common







