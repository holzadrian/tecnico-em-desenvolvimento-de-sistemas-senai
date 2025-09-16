nomes = ["Lucas", "Jão", "Pedro", "Lara"]

nome_usuario = input("Digite um nome: ")

if nome_usuario in nomes:
    print(f"O nome {nome_usuario} esta na lista.")
else:
    print(f"O nome {nome_usuario} nao esta na lista.")