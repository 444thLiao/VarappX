"""
Preset configurations.
"""
from varapp.filters import filters_factory as ffac



def Preset1ForFinal(name, op, val, db=None, samples_selection=None):
    filters_config= [('pass_filter', '=', 'PASS'),
                     ('aaf_1kg_all', '<=', 0.01),
                     ('aaf_exac_all', '<=', 0.01),
                     ('aaf_esp_all', '<=', 0.01),
                     ('in_dbsnp','=','true')
                      ]
    f_collection=[]
    for i,k,v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection

def Preset2ForImportant(name, op, val, db=None, samples_selection=None):
    filters_config=(('pass_filter','=','PASS'),
                  ('aaf_1kg_all','<=',0.01),
                  ('aaf_exac_all','<=',0.01),
                  ('aaf_esp_all','<=',0.01),
                    ('in_dbsnp', '=', 'true'))
    f_collection=[]
    for i,k,v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection

def Preset3ForPathogenic(name, op, val, db=None, samples_selection=None):
    filters_config=(('pass_filter','=','PASS'),
                  ('aaf_1kg_all','<=',0.01),
                  ('aaf_exac_all','<=',0.01),
                  ('aaf_esp_all','<=',0.01),
                    ('in_dbsnp', '=', 'true'))
    f_collection=[]
    for i,k,v in filters_config:
        f = ffac.variant_filters_map[i](name=i, val=v, op=k, db=db)
        f_collection.append(f)
    return f_collection









