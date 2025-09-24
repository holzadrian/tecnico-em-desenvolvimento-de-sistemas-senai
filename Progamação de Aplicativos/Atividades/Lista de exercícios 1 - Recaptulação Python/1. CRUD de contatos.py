contatos = []
def adicionar():
    nome = input("Qual é seu nome?: ")
    email = input("Qual é o seu email?: ")
    telefone = input("Qual seu telefone?: ")
    contatos.append({"nome": nome,"email": email,"telefone": telefone})
    print("Contato Adicionado baby")


def listar():
    
    print("-----Lista de contatos-----")
    if not contatos:
        print("Não há contatos cadastrados")
    for i, contato in enumerate(contatos):
        print(f"{i} - nome:{contato['nome']}, email:{contato['email']},telefone:{contato['telefone']}")

        
def buscar():
    print("-----Buscar Contato-----")
    if len(contatos) > 0:
        listar()
        indice = int(input("Qual contato voce vai buscar?: "))
        print(f"Nome: {contatos[indice]['nome']}")
        print(f"E-mail: {contatos[indice]['email']}")
        print(f"telefone: {contatos[indice]['telefone']}")
    else:
        print("Não há contatos")

def editar():
    print("-----Editar Contato-----")
    if not contatos:
        print("Não há contatos para editar")
        return
    listar()
    indice = int(input("Qual Contato voce deseja alterar"))
    if 0 <= indice < len(contatos):
    
        nome = input("Qual o novo nome?: (nao digite se n quiser mudar)")
        email = input("Qual o novo email?: (nao digite se n quiser mudar)")
        telefone = input("Qual o novo telefone?: (nao digite se n quiser mudar)")

    if nome:
        contatos[indice]['nome']= nome
    if email:
        contatos[indice]['email'] = email
    if telefone:
        contatos[indice]['telefone'] = telefone
    
    print("CONTATO EDITADO!!!")
        


def remover():
    print("-----Remover contatinho do zapzap-----")
    if not contatos:
        print("Não há contatos para se remover")
        return
    listar()
    indice = int(input("Qual Contato voce deseja remover?: "))
    if contatos:
        contatos.pop(indice)
        print("contato removido com sucesso!!")

 
def menu():
    
    print("----- Cadastro de Contatos-----")
    print("1- Adicionar contatos")
    print("2- Listar contatos")
    print("3- Buscar contatos")
    print("4- Editar contatos")
    print("5- Remover contatos")
    print("6- Sair")




opcao = 0

while opcao != 6:
    menu()
    opcao = (input("Qual opção voce deseja?: "))
    if not opcao:
        print("opçao inválida")
    elif opcao == 1:
        adicionar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        buscar()
    elif opcao == 4:
        editar()
    elif opcao == 5:
        remover()
    elif opcao == 6:
        print("Adeus parceiro!")   
    else:
        print("opção inválida") 

