class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        total = self.preco * self.quantidade
        return (f"O total do produto {self.nome} é R$ {total:.2f}.")
    
produto01 = Produto("Storm Grey Baggy Jeans", 329.90, 1)
produto02 = Produto("Ciena Horse Index Heavy", 219.00, 2)
produto03 = Produto("Nike Air Max Fire", 899.99, 5)

print(produto01.calcular_total())
print(produto02.calcular_total())
print(produto03.calcular_total())