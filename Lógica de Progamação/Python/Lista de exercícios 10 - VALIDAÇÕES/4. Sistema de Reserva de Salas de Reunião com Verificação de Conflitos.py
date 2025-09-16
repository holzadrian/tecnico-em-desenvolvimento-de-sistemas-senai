from datetime import datetime

salas_disponiveis = ["Sala de Reunião 1", "Sala de Reunião 2", "Auditório"]
reservas = []

while True:
    responsavel = input("Digite seu nome ou 'sair' para encerrar: ")

    if responsavel.lower() == "sair":
        break

    if responsavel == "":
        print("Erro: Insira um nome válido. Tente novamente.\n")
        continue

    while True:
        print("Salas disponíveis:")
        for i, sala in enumerate(salas_disponiveis, 1):
            print(f"{i} - {sala}")

        sala_escolha = input("Digite o número da sala desejada: ").strip()
        if not sala_escolha.isdigit() or not (1 <= int(sala_escolha) <= len(salas_disponiveis)):
            print("Erro: Número de sala inválido.\n")
            continue

        sala = salas_disponiveis[int(sala_escolha) - 1]
        break
    
    while True:
        data_input = input("Data da reserva (DD/MM/AAAA): ").strip()
        try:
            data_formatada = datetime.strptime(data_input, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Erro: Data inválida.\n")
            continue

    while True:
        horario_input = input("Horário da reserva (HH:MM): ").strip()
        try:
            horario_formatado = datetime.strptime(horario_input, "%H:%M").time()
        except ValueError:
            print("Erro: Horário inválido.\n")
            continue

        conflito = False
        for r in reservas:
            if r['sala'] == sala and r['data'] == data_input and r['horario'] == horario_input:
                conflito = True
                

        if conflito:
            print("Erro: Essa sala já está reservada para essa data e horário.\n")
            continue

        reservas.append({
            "responsavel": responsavel,
            "sala": sala,
            "data": data_input,
            "horario": horario_input
        })
        print("Reserva confirmada com sucesso!\n")
        break

reservas.sort(key=lambda r: datetime.strptime(r['data'] + " " + r['horario'], "%d/%m/%Y %H:%M"))

print("\nReservas Confirmadas:")
for r in reservas:
    print(f"{r['data']} às {r['horario']} - {r['sala']} - Responsável: {r['responsavel']}")