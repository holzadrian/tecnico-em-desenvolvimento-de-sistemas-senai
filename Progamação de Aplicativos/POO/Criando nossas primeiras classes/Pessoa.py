class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return (f"Olá! O meu nome é {self.nome} e eu tenho {self.idade} anos.")

    def fazer_aniversario(self):
        self.idade += 1
        return (f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")

    def e_maior_de_idade(self):
        if self.idade >= 18:
            return (f"{self.nome} é maior de idade.")
        else:
            return (f"{self.nome} é menor de idade.")

id01 = Pessoa("Adrian", 17)
id02 = Pessoa("Gustavo", 16)
id03 = Pessoa("Emanuel", 16)

print(id01.apresentar())
print(id02.fazer_aniversario())
print(id03.e_maior_de_idade())