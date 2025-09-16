notas = []
resposta = int(input("Digite quantos alunos você tem: "))
for i in range(1, resposta + 1):
    notas.append (float(input(f"Digite a nota do aluno {i}: ")))
media = sum(notas) / resposta
acima = 0
for i in range(0, resposta): 
    if notas[i] >= media:
        acima += 1
print(f"\nA média é: {media}")
print(f"{acima} alunos ficaram acima da média.")