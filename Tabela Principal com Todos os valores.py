import tkinter as tk
from tkinter import ttk
import pandas as pd
from tabulate import tabulate

# Cria a janela principal
root = tk.Tk()
root.title("Tabela de Energia Mundial")
root.configure(background='blue')  # Define o fundo azul

# Lê o arquivo CSV e define o separador como ';'
dataframe = pd.read_csv('Energia Mundial.csv', sep=';')

# Remove a coluna vazia
dataframe = dataframe.dropna(axis=1, how='all')

# Trata colunas vazias e valores ausentes
dataframe.fillna("", inplace=True)

# Renomeia as colunas sem rótulos definidos
dataframe.columns = [f"Coluna {i}" if "Unnamed" in str(col) else col for i, col in enumerate(dataframe.columns)]

# Converte o DataFrame em uma lista de dicionários
data = dataframe.to_dict(orient='records')

# Cria o Treeview com estilo de fundo azul
tree = ttk.Treeview(root, columns=list(data[0].keys()), show="headings", style="Blue.Treeview")

# Define as colunas e cabeçalhos
for column in data[0].keys():
    tree.heading(column, text=column)
    tree.column(column, width=100)

# Insere os dados na tabela
for item in data:
    tree.insert("", "end", values=list(item.values()))

# Define o estilo do Treeview com fundo azul
style = ttk.Style()
style.configure("Blue.Treeview", background="blue", foreground="white", fieldbackground="blue")

# Define o estilo para o cabeçalho da tabela
style.configure("Blue.Treeview.Heading", background="blue", foreground="black")

# Adiciona o Treeview à janela principal
tree.pack(fill="both", expand=True)

# Inicia o loop principal
root.mainloop()
