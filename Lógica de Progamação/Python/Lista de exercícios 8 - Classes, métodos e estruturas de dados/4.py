lista = [1, 2, 3, 4, 5]
def inverte_lista(l: list):
    novo_vetor = []
    indice = 0
    tamanho_total = len(l)
    for _ in l:
        indice_reverso = tamanho_total - indice - 1
        novo_vetor.append(l[indice_reverso])
        indice = indice + 1
    return novo_vetor

print(inverte_lista(lista))