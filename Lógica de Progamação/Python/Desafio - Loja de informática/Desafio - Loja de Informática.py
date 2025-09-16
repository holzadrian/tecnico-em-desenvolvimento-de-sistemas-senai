produtos = []
resposta = 0

while resposta != 5:

    print("=== Loja de Informática ===\n1 - Cadastrar Produto\n2 - Listar Produtos\n3 - Realizar Venda\n4 - Relatório do Dia\n5 - Sair")
    resposta = int(input("Escolha: "))

    if resposta == 1:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        produto = {
            "nome": nome,
            "preco":preco
        }
        produtos.append(produto)

    elif resposta == 2:
        for i, produto in enumerate(produtos, 0):
            print(f"{i} - {produto["nome"]} - {produto["preco"]}")
            continue

    elif resposta == 3:
        for i, produto in enumerate(produtos, 0):
            print(f"{i} - {produto["nome"]} - {produto["preco"]}")
        nvendido = int(input("Qual produto deseja vender: "))
        pvendido = produtos[nvendido]
        total = total + pvendido["preco"]
        vendido = vendido + 1
    
    elif resposta == 4:
        print(f"O total vendido foi R${total}")
        print(f"A quantidade de itens vendidos foi {vendido}")

        if total > 1000:
            print("Ótimo trabalho hoje! Bateu a meta de R$1000!")
    
    elif resposta == 5:
        print ("volte sempre!")