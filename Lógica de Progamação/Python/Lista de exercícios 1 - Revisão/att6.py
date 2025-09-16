fretes = {
    "SP": 20.00,
    "RJ": 24.50,
    "MJ": 40.25,
    "BA": 47.15
}

print("Opções de estados disponíveis para entregar:")
print("1 - SP")
print("2 - RJ")
print("3 - MJ")
print("4 - BA")

estado = input("Digite o estado (sigla): ").upper()

if estado in fretes:
    print(f"O valor do frete para {estado} é R${fretes[estado]:.2f}")
else:
    print("Desculpe, não será possível fazer a entrega para esse estado.")