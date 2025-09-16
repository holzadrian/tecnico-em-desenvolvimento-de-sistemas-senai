valor = float(input("Me informe o valor da sua compra: "))

if valor > 100:
    valor_total = valor - 15
    
else:
    valor_total = valor -5

print(f"Parabéns você ganhou um desconto! Sua compra deu {valor_total} reais.")