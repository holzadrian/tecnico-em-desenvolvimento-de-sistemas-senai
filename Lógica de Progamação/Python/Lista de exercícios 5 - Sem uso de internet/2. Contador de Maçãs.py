macaspordia = []

for i in range(1, 4):
    quantidade =int(input(f"Digite o número de maçãs colhidas no dia {i}: "))
    macaspordia.append(quantidade)

total_macas = sum(macaspordia)

media_macas = total_macas / 3

maior_quantidade = max(macaspordia)

dia_maior = macaspordia.index(maior_quantidade) + 1

print(f"Total de maçãs colhidas nos 3 dias: {total_macas}")
print(f"Média diária de maçãs colhidas: {media_macas:.2f}")
print(f"Dias com maior quantidade de maçãs: Dia {dia_maior}")