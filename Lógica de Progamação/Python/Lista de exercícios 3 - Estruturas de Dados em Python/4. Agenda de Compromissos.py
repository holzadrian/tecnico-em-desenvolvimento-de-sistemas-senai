agenda = {}

while True:
    entrada = input("Digite o dia da semana e o compromisso (ou 'fim' para encerrar): ").strip().lower()
    
    if entrada == "fim":
        break

    partes = entrada.split(maxsplit=1)
    
    if len(partes) < 2:
        print("Entrada inválida. Use o formato: 'dia compromisso'.")
        continue

    dia, compromisso = partes[0], partes[1]

    if dia not in agenda:
        agenda[dia] = []
    agenda[dia].append(compromisso)

print("\nCompromissos cadastrados:")
for dia, compromissos in agenda.items():
    print(f"{dia.capitalize()}: {', '.join(compromissos)}")

total = sum(len(compromissos) for compromissos in agenda.values())
print(f"\nTotal de compromissos cadastrados: {total}")

dia_mais_compromissos = max(agenda, key=lambda d: len(agenda[d]))
print(f"Dia com mais compromissos: {dia_mais_compromissos.capitalize()} ({len(agenda[dia_mais_compromissos])} compromissos)")