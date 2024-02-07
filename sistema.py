menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

for _ in range(9999999):  # Um número grande para garantir que o loop rode até a opção "q" ser selecionada
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro no depósito! Valor informado inválido")
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        saldo_execedido = valor > saldo
        limite_execedido = valor > limite
        saques_execedido = numero_saques >= LIMITE_SAQUES

        if saldo_execedido:
            print("Erro na operação! Você não tem saldo suficiente")
        elif limite_execedido:
            print("Erro na operação! Você não tem limite suficiente")
        elif saques_execedido:
            print("Erro na operação! Você excedeu o limite de saques diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso")
        else:
            print("Erro na operação! Valor informado inválido")
    elif opcao == "e":
        print('               EXTRATO               ')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('                                     ')
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")