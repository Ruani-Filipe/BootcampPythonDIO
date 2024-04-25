#3 Operações - Depósito, Saque e Extrato

# Todos os depósitos devem ser armazenados em uma variável e exibir na operação do extrato
# Não pode permitir depósitos negativos

#Operação de Saque
# Máximo de 3 saques diários e com limite de R$ 500,00 por saque
# Caso não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro e os saques devem ser exibidos em uma variável na operação de extrato

# Operação de Extrato
# Deve exibir todos os depósitos e saques realizados na conta e ao final exibir o saldo atual da conta
# Exibir R$ 500,00

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            numero_depositos += 1
            extrato += f"Depósito n.º {numero_depositos}: R$ {valor:.2f}\n"
            print(f"Depósito realizado no sucesso no valor de R$ {valor:.2f}.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque n.º {numero_saques}: R$ {valor:.2f}\n"
            print(f"Saque realizado no sucesso no valor de R$ {valor:.2f}.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")