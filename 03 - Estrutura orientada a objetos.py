class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular  # objeto Cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"Titular: {self.titular.nome}")
        print(f"Conta: {self.numero}")
        print(f"Saldo: R${self.saldo:.2f}")

# Exemplo de uso
cliente1 = Cliente("Ana", "123.456.789-00", 30)
conta1 = ContaBancaria(1001, cliente1, 500.0)

conta1.depositar(200)
conta1.sacar(100)
conta1.extrato()
