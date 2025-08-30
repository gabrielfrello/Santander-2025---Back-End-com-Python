# Sistema Bancário Refatorado com Funções

# Variáveis do sistema
saldo = 0.0
extrato = []
LIMITE_SAQUE = 500.0

# Função para depósito
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

# Função para saque
def sacar(valor):
    global saldo
    if valor <= 0:
        print("Valor de saque inválido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > LIMITE_SAQUE:
        print(f"Saque excede o limite de R${LIMITE_SAQUE:.2f}.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

# Função para exibir extrato
def mostrar_extrato():
    print("\n=== EXTRATO ===")
    if extrato:
        for registro in extrato:
            print(registro)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Saldo atual: R${saldo:.2f}")
    print("================\n")

# Função principal do sistema
def sistema_bancario():
    while True:
        print("Selecione uma opção:")
        print("[d] Depósito")
        print("[s] Saque")
        print("[e] Extrato")
        print("[q] Sair")
        opcao = input().strip().lower()

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            depositar(valor)
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            sacar(valor)
        elif opcao == "e":
            mostrar_extrato()
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o sistema
sistema_bancario()
