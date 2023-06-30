import pandas as pd
import glob
d_es = glob.glob('consulta_*.csv')
list_es = []
cad_pe = pd.read_csv('consulta_cand_2022_AP.csv', sep=';', encoding='latin_1')

for d in d_es:
    var_es = pd.read_csv(d, sep=';', encoding='latin_1')
    list_es.append(var_es)

#print(list_es)

es_completo = pd.concat(list_es, axis=0, ignore_index=True)
#print(es_completo.shape)
#print(es_completo.head())
print(es_completo.describe())
print(es_completo.shape)
print(es_completo.dtypes) #
# Nome das colunas 
print(es_completo.columns)
# Organizar dados
print(es_completo.sort_values('SG_UF'))
print(es_completo[es_completo.SG_UF == 'PA'])