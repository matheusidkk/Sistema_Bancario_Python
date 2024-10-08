from datetime import datetime, timedelta


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """


def mensagem(msn):
    return (
        f"""
#####################################

{msn}

#####################################
"""
    )


def depositar(saldo, extrato, numero_transacoes, LIMITE_TRANSACOES):
    if numero_transacoes < LIMITE_TRANSACOES:
        valor = float(input("Digite o valor que deseja depositar \n=> "))
        saldo += valor
        numero_transacoes += 1
        data_hoje = datetime.now()
        extrato += f"\n{'Deposito no valor de R$'}{valor:.2f} -- {data_hoje.strftime('%d/%m/%Y - %H:%M:%S')}"
        print(mensagem(f"Valor de R${valor:.2f} depositado com sucesso, seu saldo agora é de R${saldo:.2f}"))
        return saldo, extrato, numero_transacoes
    else:
        print(mensagem("Você já realizou 10 transações hoje, retorne amanhã."))
        return saldo, extrato, numero_transacoes


def sacar(saldo, limite, extrato, numero_transacoes, LIMITE_TRANSACOES):
    if saldo > 0 and numero_transacoes < LIMITE_TRANSACOES:
        valor = float(input("Digite o valor que deseja sacar \n=> "))
        
        if valor <= saldo and valor <= limite:
            saldo -= valor
            numero_transacoes += 1
            data_hoje = datetime.now()
            extrato += f"\n{'Saque no valor de R$'}{valor:.2f} -- {data_hoje.strftime('%d/%m/%Y - %H:%M:%S')}"
            print(mensagem(f"Valor de R${valor:.2f} sacado com sucesso, seu saldo agora é de R${saldo:.2f}"))
        elif valor > limite:
            print(mensagem(f"Limite de R${limite:.2f} por saque, tente novamente"))
        else:
            print(mensagem(f"Saldo insuficiente, seu saldo é de R${saldo:.2f}"))

    elif numero_transacoes >= LIMITE_TRANSACOES:
        print(mensagem("Você já realizou 10 transações hoje, retorne amanhã."))
    else:
        print(mensagem("Você não tem saldo disponível."))

    return saldo, extrato, numero_transacoes


def exibir_extrato(extrato, saldo):
    print(f"{extrato}\n\n#####################################\n\nSaldo atual de R${saldo:.2f}")


def main():
    saldo = 600  # Saldo inicial
    limite = 500  # Limite por saque
    extrato = "############## Extrato ##############\n"  # Cabeçalho do extrato
    numero_transacoes = 0  # Contador de saques
    LIMITE_TRANSACOES = 10  # Limite de saques por dia

    while True:
        opcao = input(menu).lower()  # Solicita a opção do menu

        if opcao == "d":
            saldo, extrato, numero_transacoes = depositar(saldo, extrato, numero_transacoes, LIMITE_TRANSACOES)

        elif opcao == "s":
            saldo, extrato, numero_transacoes = sacar(saldo, limite, extrato, numero_transacoes, LIMITE_TRANSACOES)

        elif opcao == "e":
            exibir_extrato(extrato, saldo)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print(mensagem("Operação inválida, tente novamente."))


# Inicia o programa
main()
