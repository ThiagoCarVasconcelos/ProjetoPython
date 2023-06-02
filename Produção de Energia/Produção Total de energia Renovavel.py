import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator
import seaborn as sns

# Ler o arquivo CSV
dt = pd.read_csv('Energia Mundial.csv', sep=';', parse_dates=['Data'], dayfirst=True, dtype={'Produção Total de Energia Renovável': str})

# Filtrar os dados para o período desejado
start_date = '1992-12-30'
end_date = '2022-12-31'
filtered_dt = dt[(dt['Data'] >= start_date) & (dt['Data'] <= end_date)].copy()

# Remover os pontos de milhar da coluna 'Produção Total de Energia Renovável'
filtered_dt['Produção Total de Energia Renovável'] = filtered_dt['Produção Total de Energia Renovável'].str.replace('.', '').str.replace(',', '.')

# Converter a coluna 'Produção Total de Energia Renovável' para tipo float
filtered_dt['Produção Total de Energia Renovável'] = filtered_dt['Produção Total de Energia Renovável'].astype(float)

# Converter os valores do eixo y para milhares
filtered_dt['Produção Total de Energia Renovável'] = filtered_dt['Produção Total de Energia Renovável'] / 1000

# Configurar o estilo de fundo usando a seaborn API
sns.set_style('whitegrid')

# Configurar o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Definir esquema de cores
line_color = '#0f4c75'  # Azul escuro
marker_color = '#f9a826'  # Laranja

# Plotar a linha
ax.plot(filtered_dt['Data'], filtered_dt['Produção Total de Energia Renovável'], color=line_color, marker='o', markerfacecolor=marker_color, markersize=5)

# Adicionar os valores acima dos marcadores
for i, row in filtered_dt.iterrows():
    ax.text(row['Data'], row['Produção Total de Energia Renovável'], f"{row['Produção Total de Energia Renovável']:.2f}k", ha='center', va='bottom', fontsize=8, color=marker_color)

# Adicionar grade
ax.grid(True)

# Definir o intervalo dos anos no eixo x (a cada dois anos)
years = YearLocator(1)
ax.xaxis.set_major_locator(years)

# Ajustar escala do eixo y
ax.set_ylim(bottom=0, top=1200)

# Ajustar tamanho dos rótulos
ax.tick_params(axis='both', labelsize=10)

# Rotacionar os rótulos do eixo x
plt.xticks(rotation=45)

# Adicionar rótulos e título do gráfico
ax.set_xlabel('Anos', fontsize=12)
ax.set_ylabel('Produção Total de Energia Renovável (Milhares)', fontsize=12)
ax.set_title('Produção Total de Energia Renovável de 1993 a 2022', fontsize=14)

# Configurar cor de fundo
ax.set_facecolor('#f2f2f2')  # Cor de fundo cinza claro

# Exibir o gráfico
plt.tight_layout()
plt.show()
