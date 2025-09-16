# Aqui ele pede pro usuário que digite dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Aqui ele faz as contas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Aqui ele não gosta de divisão por zeroKKKKKKKKKKKKKKKKK
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Erro: Divisão por zero!!!!!!"

# E aqui ele fala os resultados
print(f"Soma: {numero1} + {numero2} = {soma}")
print(f"Subtração: {numero1} - {numero2} = {subtracao}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"Divisão: {numero1} / {numero2} = {divisao}")