# python3

import textwrap


mensagem_inicial = """
:: Banco vanTol ::
    (v2.0)
"""


def menu():

    menu_operacao = """\n
    Digite a operação desejada:

    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [Q]\tSair

    """

    return input(textwrap.dedent(menu_operacao))


def op_deposito(saldo, valor, extrato, /):
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

    return saldo, extrato


def op_saque(*, saldo, valor, extrato, saque_maximo, saques, limite_saque_diario):

    if saques >= limite_saque_diario:
        print("\n! Erro: Operação inválida!")
        print("Limite diário de saques atingido.")
        print(f"Seu limite diário de saque é de: {limite_saque_diario} saques")
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

    return saldo, extrato


def op_extrato(saldo, /, *, extrato):
    print("\n-----------")
    print("| EXTRATO |")
    print("-----------\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n-----------")


def op_nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def op_listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def op_novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    AGENCIA = "001"
    LIMITE_SAQUE_DIARIO = 3

    extrato = ""
    saldo = 10
    saque_maximo = 500
    saques = 0
    usuarios = []
    contas = []

    print(mensagem_inicial)

    while True:
        operacao = menu()

        if operacao == "d":
            print("\n------------")
            print("| DEPÓSITO |")
            print("------------\n")
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = op_deposito(saldo, valor, extrato)

        elif operacao == "s":
            print("\n---------")
            print("| SAQUE |")
            print("---------\n")
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = op_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                saque_maximo=saque_maximo,
                saques=saques,
                limite_saque_diario=LIMITE_SAQUE_DIARIO,
            )

        elif operacao == "e":
            op_extrato(saldo, extrato=extrato)

        elif operacao == "nc":
            numero_conta = len(contas) + 1
            conta = op_nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif operacao == "lc":
            op_listar_contas(contas)

        elif operacao == "nu":
            op_novo_usuario(usuarios)

        elif operacao == "Q":
            break

        else:
            print("\n! Erro: Operação inválida!")
            print("\n-----------")


main()
