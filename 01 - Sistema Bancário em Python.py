# Sistema Bancário em Python

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +{valor}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -{valor}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f"Transferência: -{valor} para {conta_destino.titular}")
            conta_destino.historico.append(f"Transferência: +{valor} de {self.titular}")
            print(f"Transferência de R${valor:.2f} para {conta_destino.titular} realizada.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

    def mostrar_historico(self):
        print(f"Histórico de {self.titular}:")
        if not self.historico:
            print("Sem movimentações.")
        for item in self.historico:
            print("-", item)

# Banco
contas = []

def criar_conta():
    nome = input("Nome do titular: ")
    conta = Conta(nome)
    contas.append(conta)
    print(f"Conta criada com sucesso para {nome}!")

def selecionar_conta():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("Contas disponíveis:")
    for i, c in enumerate(contas):
        print(f"{i} - {c.titular}")
    escolha = input("Escolha a conta pelo número: ")
    if escolha.isdigit() and int(escolha) in range(len(contas)):
        return contas[int(escolha)]
    else:
        print("Escolha inválida.")
        return None

def menu():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Criar Conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Consultar Saldo")
        print("6 - Histórico")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            conta = selecionar_conta()
            if conta:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
        elif opcao == "3":
            conta = selecionar_conta()
            if conta:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
        elif opcao == "4":
            print("Conta de origem:")
            conta_origem = selecionar_conta()
            if conta_origem:
                print("Conta de destino:")
                conta_destino = selecionar_conta()
                if conta_destino and conta_destino != conta_origem:
                    valor = float(input("Valor da transferência: "))
                    conta_origem.transferir(valor, conta_destino)
                else:
                    print("Conta de destino inválida.")
        elif opcao == "5":
            conta = selecionar_conta()
            if conta:
                conta.mostrar_saldo()
        elif opcao == "6":
            conta = selecionar_conta()
            if conta:
                conta.mostrar_historico()
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema
if __name__ == "__main__":
    menu()
