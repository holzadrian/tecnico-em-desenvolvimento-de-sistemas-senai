numeros = [1, 4, 7, 8, 10]

soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
        
print("A soma dos numeros pares é: ", soma_pares)