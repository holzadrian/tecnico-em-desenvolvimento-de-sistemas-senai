tarefas = []



def adicionartarefa():
    tarefa = input(("Qual sua Tarefa de hoje?: ")).strip()
    if not tarefa:
        print("A Tarefa não pode ser vazia")
        return
    descricao = input(("Qual a descrição de sua tarefa?(OPCIONAL): "))
    status = "pendente"
    tarefas.append({"tarefa": tarefa, "status": status, "descricao": descricao})
    print("A tarefa foi Marcada")
    
    
def listartarefa():
    print("-----Lista de Afazeres-----")
    if not tarefas:
        print("Nenhuma tarefa cadastrada")
        return
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}.{tarefa['tarefa']}-{tarefa['status']}")
    if tarefa['descricao']:
        print(f"Descrição: {tarefa['descricao']}")

def marcarconcluida():
    listartarefa()
    if not tarefas:
        print("nenhuma tarefa cadastrada")
    if len(tarefas)> 0:
        indice = int(input("Qual tarefa deseja marcar como concluida?: "))
        if 0 < indice <= len(tarefas):
            tarefas[indice -1]['status'] = 'concluida'
            print("Sua tarefa foi marcada como concluida.")
        else:
            print("numero inválido")

def removertarefa():
    print("-----Remover Tarefa-----")
    listartarefa()
    if len(tarefas) > 0:
        indice = int(input("Qual a Tarefa que deseja remover?: "))
        tarefas.pop(indice - 1)
        print("Sua tarefa foi removida")

def filtrar_por_status():
    status = input("Digite o status para filtrar (pendente/concluída): ").strip().lower()
    if status not in ["pendente", "concluída"]:
        print("Status inválido.\n")
        return
    filtradas = [t for t in tarefas if t["status"] == status]
    if not filtradas:
        print(f"Nenhuma tarefa com status '{status}'.\n")
        return
    print(f"\nTarefas com status '{status}':")
    for i, tarefa in enumerate(filtradas):
        print(f"{i + 1}. {tarefa['descricao']}")
    print()




def menu():
    print("-----Lista de Tarefas-----")
    print("1- Adicionar Tarefa📆")
    print("2- Listar Tarefas✏️")
    print("3- Marcar Tarefas como realizadas")
    print("4- Remover Tarefas")
    print("5- Filtrar tarefas por status")
    print("6- Sair")


    while True:
        escolha = int(input("Escolha uma das opções: "))
        
        if escolha == 1:
            adicionartarefa()
        elif escolha == 2:
            listartarefa()
        elif escolha == 3:
            marcarconcluida()
        elif escolha == 4:
            removertarefa()
        elif escolha == 5:
            filtrar_por_status()
        elif escolha == 6:
            print("Adeus volte sempre")
            break
        else:
            print("opção inválida. Tente novamente")
            continue    
menu()