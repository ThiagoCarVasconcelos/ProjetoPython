import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator
import seaborn as sns

# Ler o arquivo CSV
dt = pd.read_csv('../Energia Mundial.csv', sep=';', parse_dates=['Data'], dayfirst=True, dtype={'Consumo Total de Energia Primária': str})

# Filtrar os dados para o período desejado
start_date = '1992-12-31'
end_date = '2022-12-31'
filtered_dt = dt[(dt['Data'] >= start_date) & (dt['Data'] <= end_date)].copy()

# Remover os pontos de milhar da coluna 'Consumo Total de Energia Primária'
filtered_dt['Consumo Total de Energia Primária'] = filtered_dt['Consumo Total de Energia Primária'].str.replace('.', '').str.replace(',', '.')

# Converter a coluna 'Consumo Total de Energia Primária' para tipo float
filtered_dt['Consumo Total de Energia Primária'] = filtered_dt['Consumo Total de Energia Primária'].astype(float)

# Converter os valores do eixo y para milhões
filtered_dt['Consumo Total de Energia Primária'] = filtered_dt['Consumo Total de Energia Primária'] / 1000000

# Configurar o estilo de fundo usando a seaborn API
sns.set_style('whitegrid')

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Definir esquema de cores
line_color = '#0f4c75'  # Azul escuro
marker_color = '#f9a826'  # Laranja

# Plotar a linha
ax.plot(filtered_dt['Data'], filtered_dt['Consumo Total de Energia Primária'], color=line_color, marker='o', markerfacecolor=marker_color, markersize=5)

# Adicionar os valores acima dos marcadores
for i, row in filtered_dt.iterrows():
    ax.text(row['Data'], row['Consumo Total de Energia Primária'], f"{row['Consumo Total de Energia Primária']:.2f}M", ha='center', va='bottom', fontsize=8, color=marker_color)

# Adicionar grade
ax.grid(True)

# Definir o intervalo dos anos no eixo x (a cada dois anos)
years = YearLocator(1)
ax.xaxis.set_major_locator(years)

# Ajustar escala do eixo y
ax.set_ylim(bottom=0, top=10)

# Ajustar tamanho dos rótulos
ax.tick_params(axis='both', labelsize=10)

# Rotacionar os rótulos do eixo x
plt.xticks(rotation=45)

# Adicionar rótulos e título do gráfico
ax.set_xlabel('Anos', fontsize=12)
ax.set_ylabel('Consumo Total de Energia Primária (Milhões)', fontsize=12)
ax.set_title('Consumo Total de Energia Primária de 1993 a 2022', fontsize=14)

# Configurar cor de fundo
ax.set_facecolor('#f2f2f2')  # Cor de fundo cinza claro

# Exibir o gráfico
plt.tight_layout()
plt.show()
