funcionarios = []

while True:
    print("\nMenu de operações:")
    print("1. Cadastrar novo funcionário")
    print("2. Listar todos os funcionários")
    print("3. Buscar funcionário pelo nome")
    print("4. Excluir um funcionário")
    print("5. Sair")
    
    escolha = input("Escolha a operação desejada (1-5): ")

    if escolha == "1":
        nome = input("Digite o nome do novo funcionário: ")
        funcionarios.append(nome)
        print(f"Funcionário {nome} cadastrado com sucesso!")
    
    elif escolha == "2":
        if len(funcionarios) == 0:
            print("Não há funcionários cadastrados.")
        else:
            print("Lista de funcionários cadastrados:")
            for nome in funcionarios:
                print(f"- {nome}")
    
    elif escolha == "3":
        nome = input("Digite o nome do funcionário que deseja buscar: ")
        if nome in funcionarios:
            print(f"O funcionário {nome} está cadastrado.")
        else:
            print(f"O funcionário {nome} não foi encontrado.")
    
    elif escolha == "4":
        nome = input("Digite o nome do funcionário que deseja excluir: ")
        if nome in funcionarios:
            funcionarios.remove(nome)
            print(f"Funcionário {nome} excluído com sucesso!")
        else:
            print(f"O funcionário {nome} não foi encontrado.")
    
    elif escolha == "5":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")