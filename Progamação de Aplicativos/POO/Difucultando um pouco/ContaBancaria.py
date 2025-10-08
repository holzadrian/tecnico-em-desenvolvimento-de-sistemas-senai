class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = "Adrian"
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            return valor
        else:
            print("Valor de depósito inválido.")
            return

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return valor
        else:
            print("Saldo insuficiente para saque.")
            return

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        return self.saldo
    
    def menu(self):
        while True:
            print("\n=== Menu ===")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Mostrar Saldo")
            print("4. Sair")

            escolha = input("Escolha uma opção entre 1 e 4: ")

            if escolha == '1':
                valor = float(input("Digite o valor para depósito: R$"))
                self.depositar(valor)

            elif escolha == '2':
                valor = float(input("Digite o valor para saque: R$"))
                self.sacar(valor)

            elif escolha == '3':
                self.mostrar_saldo()

            elif escolha == '4':
                print("Saindo do sistema. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")