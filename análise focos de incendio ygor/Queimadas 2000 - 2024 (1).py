import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\Users\\Ygor\\Downloads\\historico_bioma_amazonia.csv")

# Renomeando a coluna de anos e removendo linhas desnecessárias para o recorte feito
df = df.rename(columns={'Unnamed: 0': 'Anos'})
df = df[~df['Anos'].isin(['Média*', 'Máximo*', 'Mínimo*', '1998', '1999', '2024'])]

# Plotando um gráfico e o formatando

plt.plot(df['Anos'], df['Total'])
plt.title('Total de focos ativos de incêndio por ano no século', fontsize = 18)
plt.xlabel("Anos", fontsize = 14)
plt.ylabel("Total de focos ativos", fontsize = 14)
plt.show()