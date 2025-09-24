class Carro:
    def __init__(self, marca, modelo, ano, ronco, desligando):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ronco = ronco
        self.desligando = desligando

    def apresentacao_tecnica(self):
        return (f"Este carro é um {self.marca} {self.modelo} do ano {self.ano}.")
    
    def ligar(self):
        return (f"O {self.modelo} está ligado. {self.ronco}")
    
    def desligar(self):
        return (f"O {self.modelo} está desligado. {self.desligando}")

carro01 = Carro("Corvette", "C7", 2014, "Vruum... Bub-bub-bub-bub...", "Bub-bub-bub-bub... pshhh...")
carro02 = Carro("Mercedes-Benz", "G63 AMG", 2020, "VROOM-ROAR... grrrrrrr...", "Grrrr... clun-clun... tic-tic-tic.")
carro03 = Carro("Lamborghini", "Huracán", 2021, "VRAAAAANG-dadada-DAAAA!", "Brrraaap-psh... tic-tic-tic-tic.")

print(carro01.apresentacao_tecnica())
print(carro02.ligar())
print(carro03.desligar())