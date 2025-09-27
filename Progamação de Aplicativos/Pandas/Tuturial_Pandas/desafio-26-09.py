import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/lukas-senai/pandas-tutorial/refs/heads/main/assets/alunos-30.csv")

# média das notas
media_notas = df["Nota"].mean()
print(f"Média das notas: {media_notas:.2f}")

# quantidade de alunos com nota maior que 7
n_alunos_nota_menor_7 = len(df[df["Nota"] < 7])
print(f"Quantidade de alunos com nota maior que 7: {n_alunos_nota_menor_7}")

# aluno mais velho com nota maior que 8
aluno_mais_velho_nota_maior_8 = df[(df["Idade"] == df["Idade"].max()) & (df["Nota"] > 8)]
print(f"\nAluno mais velho com nota maior que 8:\n {aluno_mais_velho_nota_maior_8}")