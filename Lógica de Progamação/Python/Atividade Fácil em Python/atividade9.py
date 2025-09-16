# Ele solicita pro usuário que digite as idades
idade1 = int(input("Digite a idade da primeira pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

# Dps ele compara e exibe o resultado
if idade1 > idade2:
    print("A primeira pessoa é mais velha.")
elif idade2 > idade1:
    print("A segunda pessoa é mais velha.")
else:
    print("As duas pessoas têm a mesma idade.")