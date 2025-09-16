energias = []

print("Mago, insira a energia de cada uma das 5 pedras:")

for i in range(5):
    energia = int(input(f"Digite a energia da pedra {i + 1}: "))
    energias.append(energia)

energia_total = sum(energias)

print(f"\nEnergia total acumulada: {energia_total}")