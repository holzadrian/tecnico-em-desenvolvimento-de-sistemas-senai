nomes = []
telefones = []

def adcionar():
    nome = input("Qual seu nome? ")
    nomes.append(nome)
    telefone = int(input("Qual seu número de telefone? "))
    telefones.append(telefone)

def procurar():
    pesquisa = input("Digite o nome do contato: ")
    indice = nomes.index(pesquisa)
    print(f"O telefone é {telefones[indice]}")

def listar():
    print(f"Os contatos são {nomes}\n{telefones}")

while True:
    print("=== MENU DE CADASTRO ===\n1. Adicionar Pessoas\n2. Procurar Pessoas\n3.Listar Pessoas")
    opcao = int(input("O que você quer fazer? "))
    if opcao == 1:
        adcionar()
    elif opcao == 2:
        procurar()
    elif opcao == 3:
        listar()