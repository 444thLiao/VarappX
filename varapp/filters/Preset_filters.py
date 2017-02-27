"""
Preset configurations.
"""




def Preset1ForFinal(filters: object = None, samples_selection: object = None, db: object = 'default'):
    filters_config= [('pass_filter', '=', 'PASS'),
                     ('aaf_1kg_all', '<=', 0.01),
                     ('aaf_exac_all', '<=', 0.01),
                     ('aaf_esp_all', '<=', 0.01
                      )]

    return filters_config

def Preset2ForImportant(filters: object = None, samples_selection: object = None, db: object = 'default'):
    filters_config=(('pass_filter','=','PASS'),
                  ('aaf_1kg_all','<=',0.01),
                  ('aaf_exac_all','<=',0.01),
                  ('aaf_esp_all','<=',0.01)
                   )

    return filters_config

def Preset3ForPathogenic(filters: object = None, samples_selection: object = None, db: object = 'default'):
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







