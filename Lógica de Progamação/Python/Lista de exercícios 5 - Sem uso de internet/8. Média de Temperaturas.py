total = 0
maior = 0
quente = 0

for dia in range(1, 4):
    temperatura = float(input(f"Digite a temperatura do dia {dia}: "))

    total = total + temperatura

    if temperatura > maior or dia == 1:
        maior = temperatura
        quente = dia

print(f"A média das temperaturas é {total / 3:.2f}°C.")
print(f"A maior temperatura registrada foi: {maior:.2f}°C.")
print(f"O dia mais quente foi {quente}")