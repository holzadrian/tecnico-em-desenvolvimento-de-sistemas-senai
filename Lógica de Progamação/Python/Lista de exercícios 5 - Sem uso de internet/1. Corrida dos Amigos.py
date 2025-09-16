primeiro = float(input("Irforme o tempo do primeiro corredor: "))
segundo = float(input("Irforme o tempo do segundo corredor: "))
terceiro = float(input("Irforme o tempo do terceiro corredor: "))

if primeiro < segundo and terceiro:
    print(f"O primeiro corredor é o ganhador com {primeiro} segundos!")

elif segundo < primeiro and terceiro:
    print(f"O segundo corredor é o ganhador com {segundo} segundos!")

elif terceiro < primeiro and segundo:
    print(f"O terceiro corredor é o ganhador com {terceiro} segundos!")

else:
    print("Empate!")