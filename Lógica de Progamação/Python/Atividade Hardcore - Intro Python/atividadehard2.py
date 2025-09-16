codigo1 = 0
codigo2 = 6
codigo3 = 0

tentativas_restantes = 5

while tentativas_restantes > 0:
    print(f"\nTentativas restantes: {tentativas_restantes}")
    try:
        entrada1 = int(input("Digite o primeiro código: "))
        if entrada1 != codigo1:
            print("Código incorreto!")
            tentativas_restantes -= 1
            continue

        entrada2 = int(input("Digite o segundo código: "))
        if entrada2 != codigo2:
            print("Código incorreto!")
            tentativas_restantes -= 1
            continue

        entrada3 = int(input("Digite o terceiro código: "))
        if entrada3 != codigo3:
            print("Código incorreto!")
            tentativas_restantes -= 1
            continue
        
        print("✅ Bomba desativada com sucesso!")
        break

    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        continue

if tentativas_restantes == 0:
    print("❌ BOOM! Você falhou ao desativar a bomba.")