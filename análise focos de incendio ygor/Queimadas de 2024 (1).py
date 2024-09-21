import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\Users\\Ygor\\Downloads\\historico_bioma_amazonia.csv")

# Tratamento dos dados: renomeando colunas e selecionando os dados dos meses de 2024
df = df.rename(columns={'Unnamed: 0': 'Anos'})
data_2024 = df[df['Anos'] == '2024'][['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto']]

# Criando listas/arrays para fazer o gráfico
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto']
valores = data_2024.values[0]

# Criando e formatando um gráfico
plt.figure(figsize=(8, 5))
plt.bar(meses, valores)
plt.title('Total de focos ativos de incêndio mensais em 2024', fontsize = 18)
plt.xlabel('Mês', fontsize = 14)
plt.xticks(fontsize=14)
plt.ylabel('Total de focos ativos', fontsize = 14)
plt.show()