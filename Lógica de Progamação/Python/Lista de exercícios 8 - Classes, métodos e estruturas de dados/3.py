lista = [1, 2, 3, 4, 5]
valor = 1
def indice(l, v):
    indice = 0
    for valor in l:
        if valor == v:        
            return indice
        indice = indice + 1
        
resposta = indice(lista, valor)
print(f"A valor {valor} esta na posiçao {resposta}")