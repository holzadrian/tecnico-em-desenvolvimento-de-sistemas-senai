fila = []

while True:
    entrada = input("Digite o nome do cliente e se ele prefere 'sentado' ou 'em pé' (ou 'fim' para encerrar): ").strip()
    
    if entrada.lower() == "fim":
        break

    partes = entrada.split(maxsplit=1)
    if len(partes) != 2:
        print("Formato inválido. Use: nome 'sentado' ou 'em pé'")
        continue

    nome, preferencia = partes
    preferencia = preferencia.lower()

    if preferencia == "sentado":
        fila.insert(0, nome)
    elif preferencia == "em pé":
        fila.append(nome)
    else:
        print("Preferência inválida. Use 'sentado' ou 'em pé'.")

print("\n Fila do Café ")
print(" Ordem da fila:", " -> ".join(fila))
if fila:
    print(f" Primeiro cliente: {fila[0]}")
    print(f" Último cliente: {fila[-1]}")
    print(f" Total de clientes na fila: {len(fila)}")
else:
    print("A fila está vazia.")
