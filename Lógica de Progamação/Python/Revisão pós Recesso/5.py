alunos = [("Adrian", 2.9),("Gustavo", 9.5),("Emanuel", 4.9),("Vitor", 0.8),("Erick", 7.9)]

print("Alunos acima da média:")
for nome, nota in alunos:
    if nota >= 7:
        print(nome)