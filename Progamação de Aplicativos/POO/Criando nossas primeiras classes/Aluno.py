class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 6:
            return (f"{self.nome} está aprovado(a).")
        else:
            return (f"{self.nome} está reprovado(a).")

aluno01 = Aluno("Adrian", 7)
aluno02 = Aluno("Gustavo", 2)
aluno03 = Aluno("Emanuel", 10)

print(aluno01.verificar_aprovacao())
print(aluno02.verificar_aprovacao())
print(aluno03.verificar_aprovacao())
