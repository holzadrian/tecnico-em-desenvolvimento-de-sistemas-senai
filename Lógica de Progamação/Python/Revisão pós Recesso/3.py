numeros = []
numeracao = 1
for i in range(5):
    numero = float(input(f"{numeracao}. Digite qualquer número: "))
    numeros.append(numero)
    numeracao += 1

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A média dos números é: {media}")