compromissos = []
print("Seja bem vindo ao sistema simples de agendamento de compromissos.")

while True:
    descricao = input("Digite uma breve descrição para seu compromisso: ")

    if descricao.lower() == "sair":
        break

    if descricao == "":
        print("Erro: Insira uma descrição válida. Tente novamente.\n")
        continue
        
    while True:
        dia_str = input("Digite o dia: ")
        if dia_str == "":
            continue
        dia = int(dia_str)
        if 0 > dia or dia > 31:
            print("Erro: Insira um dia válido. Tente novamente.\n")
            continue
        else:
            break

    while True:
        mes_str = input("Digite o mês: ")
        if mes_str == "":
            continue
        mes = int(mes_str)
        if 0 > mes or mes > 12:
            print("Erro: Insira um mês válido. Tente novamente.\n")
            continue
        else:
            break
    
    while True:
        ano_str = input("Digite o ano: ")
        if ano_str == "":
            continue
        ano = int(ano_str)
        if ano < 2025:
            print("Erro: Insira um mês válido. Tente novamente.\n")
            continue
        else:
            break

            
    compromissos.append({
        "Descrição": descricao,
        "Dia": dia,
        "Mês": mes,
        "Ano": ano
    })
    print(f"O compromisso {descricao} foi cadastrado com sucesso.\n")

print("\nLista dos compromissos cadastrados:\n")
for p in compromissos:
    print(f"- {p['Descrição']}: {p['Dia']}/{p['Mês']}/{p['Ano']}.")