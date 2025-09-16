# Pede ao usuário que fale um numero qlqr
numero = int(input("Digite um número para ver a tabuada: "))

# Dps mostra a tabuada do numero que ele digitou
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")