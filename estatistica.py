import pandas as pd
import glob

dados_ap_pa = ['base_dados/consulta_cand_2020_AP.csv', 'base_dados/consulta_cand_2020_PA.csv']

list_df = []

for d_status in dados_ap_pa:
    df_estado = pd.read_csv(d_status, sep=';', encoding='latin_1')
    list_df.append(df_estado)

df_completo = pd.concat(list_df, axis=0, ignore_index=True)
df_vereadores = df_completo[df_completo['CD_CARGO'] == 13].copy()

print(df_vereadores.columns)
print(df_vereadores['SG_PARTIDO'].mode())
print(df_vereadores['NR_IDADE_DATA_POSSE'].median())
print(df_vereadores['NR_IDADE_DATA_POSSE'].var())
print(df_vereadores['NR_IDADE_DATA_POSSE'].std())