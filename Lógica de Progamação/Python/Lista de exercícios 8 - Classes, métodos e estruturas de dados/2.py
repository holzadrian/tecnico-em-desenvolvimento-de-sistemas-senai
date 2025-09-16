Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, -5]
def maior(v):
    maior_numero = 0
    for i in v:
        if i > maior_numero:
            maior_numero = i
    return maior_numero

print(f"O maior número é: {maior(Lista)}")