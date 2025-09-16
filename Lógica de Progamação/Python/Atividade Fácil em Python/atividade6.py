# Ele solicita pro usuario que fale 3 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Aqui ele calcula a média com as 3 notas
media = (nota1 + nota2 + nota3) / 3

# Diz a média e o resultado
print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")