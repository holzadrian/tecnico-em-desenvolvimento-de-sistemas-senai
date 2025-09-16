soma_positivos = 0
qunt_negativos = 0

qunt_numeros = int(input("Quantos números você que digitar? "))
for i in range(1, qunt_numeros + 1):
    numero = int(input("Digite um número: "))

    if numero > 0:
        soma_positivos += numero

    if numero < 0:
        qunt_negativos += 1

print(f"A soma dos números positivos é {soma_positivos}")
print(f"A quantidade de números negativos é {qunt_negativos}")