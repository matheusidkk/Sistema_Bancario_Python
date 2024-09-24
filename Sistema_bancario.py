menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

def mensagem(msn):
    return(
f"""

#####################################

{msn}

#####################################

""")

saldo = 600  # Saldo inicial
limite = 500  # Limite por saque
extrato = "############## Extrato ##############\n"  # Cabeçalho do extrato
numero_saques = 0  # Contador de saques
LIMITE_SAQUES = 3  # Limite de saques por dia

# Loop principal do sistema
while True:
    
    opcao = input(menu).lower()  # Solicita a opção do menu
    
    # Depósito
    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar \n=> "))
        saldo += valor
        extrato += f"\n{f'Depósito no valor de R${valor:.2f}':^37}"  # Adiciona depósito ao extrato
        print(mensagem(f"Valor de R${valor:.2f} depositado com sucesso, seu saldo agora é de R${saldo:.2f}"))
    
    # Saque
    elif opcao == "s":
        if saldo > 0 and numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor que deseja sacar \n=> "))
            
            # Verifica saldo e limite de saque
            if valor <= saldo and valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f"\n{f'Saque no valor de R${valor:.2f}':^37}"  # Adiciona saque ao extrato
                print(mensagem(f"Saque concluído com sucesso, seu saldo atual é de R${saldo:.2f}"))
            elif valor > limite:
                print(mensagem(f"Limite de R${limite:.2f} por saque, tente novamente"))
            else:
                print(mensagem(f"Saldo insuficiente, seu saldo é de R${saldo:.2f}"))
        
        elif numero_saques >= LIMITE_SAQUES:
            print(mensagem("Você já realizou 3 saques hoje, retorne amanhã."))
        else:
            print(mensagem("Você não tem saldo disponível."))
    
    # Exibir extrato
    elif opcao == "e":
        print(f"{extrato}\n\n#####################################\n\nSaldo atual de R${saldo:.2f}")
    
    # Sair
    elif opcao == "q":
        break
    
    # Operação inválida
    else:
        print(mensagem("Operação inválida, tente novamente."))
