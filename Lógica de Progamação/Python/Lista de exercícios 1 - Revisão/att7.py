nome = input("Digite seu nome para gerar a chave digital: ")

if len(nome) <= 10:
    print(f"Chave gerada com sucesso para: {nome}")
else:
    print("Erro: o nome excede o limite de 10 caracteres. A chave não será gerada.")