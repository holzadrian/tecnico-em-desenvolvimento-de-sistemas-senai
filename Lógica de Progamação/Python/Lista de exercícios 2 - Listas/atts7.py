numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for numeros in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
print("Números pares: ", pares)
print("Númerps impares: ", impares)