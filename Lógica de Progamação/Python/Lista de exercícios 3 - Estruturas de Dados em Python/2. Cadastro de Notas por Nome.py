nomes = []
notas = []

while True:
    entrada = input("Digite o nome e a nota do aluno ou 'FIM' para encerrar: ")
    if entrada == "fim":
        break
    
    nome, nota = entrada.split()
    nomes.append(nome)
    notas.append(float(nota))
        
media = sum(notas) / len(notas)

maior = max(notas)
indice = notas.index(maior)
melhor_aluno = nomes[indice]
        
print("Média:", media)
print("Melhor aluno:", melhor_aluno, "com nota", maior)
print("Todos os alunos:")
for i in range(len(nomes)):
    print(nomes[i], "-", notas[i])
    