nome = input("Digite seu nome completo: ")

nomao = nome.upper()
print(nomao)

n1 = nome.split()
n2 = n1[0]
print(f"O seu primeiro nome é: {n2}")

contaletras = nome.replace(" ", "")
nomesemespaço = len(contaletras)
print(f"O seu nome tem {nomesemespaço} letras")