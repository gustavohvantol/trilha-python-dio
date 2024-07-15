# python3

mensagem_inicial = """
:: Banco vanTol ::
     (v1.0)
"""

menu_operacao = """
Digite a operação desejada:

[d] Depósito
[s] Saque
[e] Extrato
[Q] Sair

"""

extrato = ""
saldo = 10
saque_maximo = 500
saques = 0
LIMITE_SAQUE_DIARIO = 3


def op_deposito():
    global saldo, extrato

    print("\n------------")
    print("| DEPÓSITO |")
    print("------------\n")

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"+ DEPÓSITO: R$ {valor:.2f}\n"

        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        print("\n-----------")

    else:
        print("\n! Erro: Operação inválida!")
        print("O valor informado é inválido.")
        print("\n-----------")


def op_saque():
    global saldo, extrato, saque_maximo, saques, LIMITE_SAQUE_DIARIO

    print("\n---------")
    print("| SAQUE |")
    print("---------\n")

    valor = float(input("Informe o valor do saque: "))

    if saques >= LIMITE_SAQUE_DIARIO:
        print("\n! Erro: Operação inválida!")
        print("Limite diário de saques atingido.")
        print(f"Seu limite diário de saque é de: {LIMITE_SAQUE_DIARIO} saques")
        print("\n-----------")

    elif valor > saque_maximo:
        print("\n! Erro: Operação inválida!")
        print(f"O valor do seu limite para saque é de: R$ {saque_maximo:.2f}")
        print("\n-----------")

    elif valor > saldo:
        print("\n! Erro: Operação inválida!")
        print("Saldo insuficiente.")
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        print("\n-----------")

    elif valor > 0:
        saldo -= valor
        saques += 1
        extrato += f"- SAQUE: R$ {valor:.2f}\n"

        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
        print("\n-----------")

    else:
        print("\n! Erro: Operação inválida!")
        print("O valor informado é inválido.")
        print("\n-----------")


def op_extrato():
    global saldo, extrato

    print("\n-----------")
    print("| EXTRATO |")
    print("-----------\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n-----------")


print(mensagem_inicial)


while True:
    operacao = input(menu_operacao)
    if operacao == "d":
        op_deposito()
    elif operacao == "s":
        op_saque()
    elif operacao == "e":
        op_extrato()
    elif operacao == "Q":
        break
    else:
        print("\n! Erro: Operação inválida!")
        print("\n-----------")
