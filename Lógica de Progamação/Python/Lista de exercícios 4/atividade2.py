aventuras = {}

while True:
    entrada = input("Digite o dia da semana e a aventura (ou 'fim' para encerrar): ").strip()
    
    if entrada.lower() == "fim":
        break

    partes = entrada.split(maxsplit=1)
    if len(partes) < 2:
        print("Entrada inválida. Use o formato: 'dia aventura'")
        continue

    dia, aventura = partes
    dia = dia.lower()

    if dia not in aventuras:
        aventuras[dia] = []

    aventuras[dia].append(aventura)

total_aventuras = sum(len(lista) for lista in aventuras.values())
dia_mais_cheio = max(aventuras, key=lambda d: len(aventuras[d])) if aventuras else ""

print("\n Diário de Aventuras")
print(f" Total de aventuras registradas: {total_aventuras}")
print(f" Dia com mais aventuras: {dia_mais_cheio.capitalize()}")

print("\n Aventuras por dia:")
for dia, lista in aventuras.items():
    print(f"  {dia.capitalize()}:")
    for item in lista:
        print(f"    - {item}")
