print("Cardápio de sucos: ")
print("1 - Suco de Laranja")
print("2 - Suco de Uva")
print("3 - Suco de Morango")
print("4 - Suco de Abacaxi")

resposta = int(input("Digite o número desejado: "))

if resposta == 1:
    print("Você escolheu suco de laranja")
elif resposta == 2:
    print("Você escolheu suco de Uva")
elif resposta == 3:
    print("Você escolheu suco de Morango")
elif resposta == 4:
    print("Você escolheu suco de Abacaxi")
else:
    print("Opção inválida...")