import pandas as pd

df = pd.read_excel('lista.xlsx')

#1
#print(df)

#2
# print(df.info()) # mostra contagem e tipos de dados
# print(df.dtypes) # tipos de colunas
# print(df.describe()) # resumo estatístico (média, desvio, min, max)
# print(df["Nome"]) # coluna específica
# print(df[["Nome", "Idade"]]) # múltiplas colunas
# print(df.iloc[0]) # primeira linha
# print(df.iloc[0:3]) # primeiras 3 linhas

#3
# Cálculos básicos
# media_notas = df["Nota"].mean()
# meidana = df["Nota"].median()
# desvio_padrao = df["Nota"].std()

#4
# Filtragem
# maiores_de_idade = df[df["Idade"] > 18]
# aprovados = df[df["Nota"] >= 7]
# reprovados = df[df["Nota"] < 7]

# maiores_de_idade_aprovados = df[(df["Idade"] >- 18) & (df["Nota"] >= 7)]
# maiores_de_idade_reprovados = df[(df["Idade"] > 18) & (df["Nota"] < 7)]

# print("Maiores de idade:\n", maiores_de_idade)
# print("\nAprovados:\n", aprovados)
# print("\nReprovados:\n", reprovados)
# print("\nMaiores de idade aprovados:\n", maiores_de_idade_aprovados)
# print("\nMaiores de idade reprovados:\n", maiores_de_idade_reprovados)

#5
# Ordenação
# ordenado_por_nome = df.sort_values(by="Nome")
# ordenado_por_idade = df.sort_values(by="Idade")
# ordenado_por_nota_desc = df.sort_values(by="Nota", ascending=False)

# print("\nOrdenados por Nome:\n",ordenado_por_nome)
# print("\nOrdenados por Idade:\n",ordenado_por_idade)
# print("\nOrdenados por Nota(decresente):\n",ordenado_por_nota_desc)

#6
# Criando nova coluna
# df["Aprovado"] = df["Nota"] >= 7
# print(df)