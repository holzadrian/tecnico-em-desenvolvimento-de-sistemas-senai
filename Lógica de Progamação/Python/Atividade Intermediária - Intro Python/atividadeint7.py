compra1 = float(input("Digite o preço da primeira compra: "))
compra2 = float(input("Digite o preço da segunda compra: "))
compra3 = float(input("Digite o preço da terceira compra: "))

valores = [compra1, compra2, compra3]

maior_valor = max(valores)
menor_valor = min(valores)
total = sum(valores)

print(f"O maior gasto foi: R${maior_valor:.2f}")
print(f"O menor gasto foi: R${menor_valor:.2f}")
print(f"O total gasto foi: R${total:.2f}")