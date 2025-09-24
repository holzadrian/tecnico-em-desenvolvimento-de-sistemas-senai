class Aluno:
    def __init__(self, nome, curso, notas):
        self.nome = nome
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nova_nota):
        self.notas.append(nova_nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        media = sum(self.notas) / len(self.notas)
        return media
    
    def mostras_informacoes(self):
        return f"Nome: {self.nome}, Curso: {self.curso}, Notas: {self.notas}, Média: {self.calcular_media():.2f}"

aluno01 = Aluno("Adrian", "Engenharia", [])
aluno02 = Aluno("Gustavo", "Medicina", [])

aluno01.adicionar_nota(8.5)
aluno01.adicionar_nota(7.0)
print(aluno01.mostras_informacoes())
aluno02.adicionar_nota(9.0)
aluno02.adicionar_nota(6.5)
print(aluno02.mostras_informacoes())