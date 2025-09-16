Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, -5]
def soma(v):
    somatotal = 0
    for i in v:
        somatotal += i
    return somatotal

print(f"A soma é: {soma(Lista)}")