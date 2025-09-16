numeros = []

while True:
    entrada = (input("Digite qualquer número INTEIRO ou digite 'FIM' para encerrar: \n")).strip().lower()
    if entrada == "Fim":
        break
    else:
        numeros.append(int(entrada))
if numeros:
    print(f"\nTotal: {len(numeros)}")
    print(f"Média: {sum(numeros)/len(numeros):2f}")
    print(f"Maior: {max(numeros)}")
    print(f"Menor: {min(numeros)}\n")
else:
    print("Nenhum número inteiro foi digitado.")