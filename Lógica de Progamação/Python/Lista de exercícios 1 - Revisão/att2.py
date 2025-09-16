temperatura = float(input("Vamos pousar e a Capitã Byte precisa saber qual o status da temperatura do planeta: "))

if temperatura < 17: 
    print("O status do planeta é: Frio")
elif temperatura > 35:
    print("O status do planeta é: Quente")
else:
    print("O status do planeta é: Agradável")