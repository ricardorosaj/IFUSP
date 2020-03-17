import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df_1 = pd.read_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_com_desv_pad/vermelho_20_com_std.txt', sep='\t')
df_2 = pd.read_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_com_desv_pad/vermelho_40_com_std.txt', sep='\t')
df_3 = pd.read_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_com_desv_pad/vermelho_60_com_std.txt', sep='\t')
df_4 = pd.read_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_com_desv_pad/vermelho_80_com_std.txt', sep='\t')
df_5 = pd.read_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_com_desv_pad/vermelho_100_com_std.txt', sep='\t')
df = pd.read_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_txt/violeta_20.txt', sep='\t')

new_df = {'Tensao_(V)':[],'Corrente_(A)':[],"Sigma_corrente_(A)":[]}

valores_corrente_pra_varios_df = []

for i in range(len(df_1)):
    new_df['Tensao_(V)'].append(df['Tensao_[V]'][i])
    new_df['Corrente_(A)'].append(df['Corrente_[A]'][i])
    valores_corrente_pra_varios_df.extend([[df_1['Corrente_[A]'][i],df_2['Corrente_[A]'][i]],df_3['Corrente_[A]'][i],df_4['Corrente_[A]'][i]])
    std = np.std(valores_corrente_pra_varios_df)
    new_df['Sigma_corrente_(A)'].append(std[0])
    valores_corrente_pra_varios_df = []

pd.DataFrame.from_dict(new_df).to_csv('/home/ricardo/Área de Trabalho/Estudo/lab/Semana_2/arquivos_com_desv_pad/violeta_20_com_std.txt', sep='\t',index=False)

curva_1 = plt.plot(df_1['Tensao_(V)'],df_1['Corrente_(A)'],label='20%')
curva_2 = plt.plot(df_2['Tensao_(V)'],df_2['Corrente_(A)'],label='40%')
curva_3 = plt.plot(df_3['Tensao_(V)'],df_3['Corrente_(A)'],label='60%')
curva_4 = plt.plot(df_4['Tensao_(V)'],df_4['Corrente_(A)'],label='80%')
curva_5 = plt.plot(df_5['Tensao_(V)'],df_5['Corrente_(A)'],label='100%')

plt.legend(['20%','40%','60%','80%','100%'],loc='upper left')
plt.title('Vermelho')
plt.xlabel("Voltagem (V)")
plt.ylabel("Corrente (A)")
plt.grid()
plt.show()

