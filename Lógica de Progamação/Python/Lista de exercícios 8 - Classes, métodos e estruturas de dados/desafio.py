class Pilha:
    def __init__(self, nome):
        self.nome = nome
        self.pilha = []

    def empilhar(self, item):
        self.pilha.append(item)

    def desempilhar(self):
        return self.pilha.pop()

    def topo(self):
        return self.pilha[-1]

    def vazia(self):
        return self.tamanho() == 0

    def tamanho(self):
        return len(self.pilha)

    def esvazia(self):
        self.pilha.clear()

def inverte_lista(vetor: list):
    p = Pilha("p")
    novo_vetor = []

    for item in vetor:
        p.empilhar(item)

    while not p.vazia():
        novo_vetor.append(p.desempilhar())

    return novo_vetor

print(inverte_lista([1, 2, 3, 4, 5]))