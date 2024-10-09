from datetime import datetime

# Menu principal do sistema bancário
MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Deslogar
[t] Trocar conta
[x] Sair do sistema
=> """


def mensagem(texto):
    """Exibe uma mensagem formatada."""
    return (
        f"""
#####################################

{texto}

#####################################
"""
    )


def depositar(conta):
    """Realiza o depósito na conta."""
    if conta["numero_transacoes"] < 10:
        try:
            valor = float(input("Digite o valor que deseja depositar ou /x para voltar\n=> "))
            if valor == '/x':
                return
            conta["saldo_conta"] += valor
            conta["numero_transacoes"] += 1
            data_hoje = datetime.now()
            conta["extrato"].append(f"Depósito de R${valor:.2f} em {data_hoje.strftime('%d/%m/%Y - %H:%M:%S')}")
            print(mensagem(f"Valor de R${valor:.2f} depositado com sucesso, seu saldo agora é de R${conta['saldo_conta']:.2f}"))
        except ValueError:
            print(mensagem("Valor inválido. Por favor, insira um número."))
    else:
        print(mensagem("Você já realizou 10 transações hoje, retorne amanhã."))


def sacar(conta, limite):
    """Realiza o saque da conta, respeitando o limite."""
    if conta["saldo_conta"] > 0 and conta["numero_transacoes"] < 10:
        try:
            valor = float(input("Digite o valor que deseja sacar ou /x para voltar\n=> "))
            if valor == '/x':
                return
            
            if valor <= conta["saldo_conta"] and valor <= limite:
                conta["saldo_conta"] -= valor
                conta["numero_transacoes"] += 1
                data_hoje = datetime.now()
                conta["extrato"].append(f"Saque de R${valor:.2f} em {data_hoje.strftime('%d/%m/%Y - %H:%M:%S')}")
                print(mensagem(f"Valor de R${valor:.2f} sacado com sucesso, seu saldo agora é de R${conta['saldo_conta']:.2f}"))
            elif valor > limite:
                print(mensagem(f"Limite de R${limite:.2f} por saque, tente novamente."))
            else:
                print(mensagem(f"Saldo insuficiente, seu saldo é de R${conta['saldo_conta']:.2f}."))
        except ValueError:
            print(mensagem("Valor inválido. Por favor, insira um número."))
    elif conta["numero_transacoes"] >= 10:
        print(mensagem("Você já realizou 10 transações hoje, retorne amanhã."))
    else:
        print(mensagem("Você não tem saldo disponível."))


def exibir_extrato(conta):
    """Exibe o extrato da conta."""
    print("############## Extrato ##############")
    for transacao in conta["extrato"]:
        print(transacao)
    print(f"\n#####################################\nSaldo atual: R${conta['saldo_conta']:.2f}")


def main(usuario, conta):
    """Função principal para operações bancárias."""
    limite_saque = 500  # Limite de saque por transação

    while True:
        opcao = input(MENU).lower()

        if opcao == "d":
            depositar(conta)

        elif opcao == "s":
            sacar(conta, limite_saque)

        elif opcao == "e":
            exibir_extrato(conta)

        elif opcao == "q":
            print("Deslogando...")
            main_user()  # Retorna ao menu de login

        elif opcao == "t":
            print("Trocando a conta...")
            break
        
        elif opcao == "x":
            print("Saindo do sistema...")
            exit()

        else:
            print(mensagem("Operação inválida, tente novamente."))


def cadastrar_usuario():
    """Realiza o cadastro de um novo usuário."""
    nome = input("Nome (ou /x para voltar)\n=> ")
    if nome == "/x":
        main_user()
        return
    nascimento = input("Data de nascimento (ou /x para voltar)\n=> ")
    if nascimento == "/x":
        main_user()
        return
    cpf = input("CPF (ou /x para voltar)\n=> ")
    if cpf == "/x":
        main_user()
        return

    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print(f"Usuário já existe: {usuario['nome']}. Deseja criar nova conta? (y/n)")
            opcao_conta = input().lower()
            if opcao_conta == 'y':
                criar_nova_conta(usuario)
            else:
                print("Operação cancelada.")
                main_user()
            return
    
    senha = input("Senha (ou /x para voltar)\n=> ")
    if senha == "/x":
        main_user()
        return
    endereco = input("Endereço (Cidade - Bairro - Rua - Número) (ou /x para voltar)\n=> ")
    if endereco == "/x":
        main_user()
        return

    # Cria um novo usuário
    novo_usuario = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "senha": senha,
        "endereco": endereco,
        "contas": [{"numero_conta": 1, "agencia": "0001", "saldo_conta": 0, "numero_transacoes": 0, "extrato": []}]
    }
    
    usuarios.append(novo_usuario)
    print("Cadastro realizado com sucesso!")
    main_user()


def criar_nova_conta(usuario):
    """Cria uma nova conta para um usuário existente."""
    while True:
        senha_tentativa = input("Informe sua senha (ou /x para voltar)\n=> ")
        if senha_tentativa == "/x":
            main_user()
            return
        if usuario["senha"] == senha_tentativa:
            nova_conta_numero = len(usuario["contas"]) + 1
            usuario["contas"].append({
                "numero_conta": nova_conta_numero,
                "agencia": "0001",
                "saldo_conta": 0,
                "numero_transacoes": 0,
                "extrato": []
            })
            print("Nova conta criada com sucesso!")
            break
        else:
            print("Senha incorreta.")
    main_user()


def main_user():
    """Gerencia o login e cadastro de usuários."""
    opcao = input(""" 
[e] Entrar 
[c] Cadastrar-se
[x] Sair do sistema
=> """).lower()

    if opcao == "e":
        logar_usuario()
    elif opcao == "c":
        cadastrar_usuario()
    elif opcao == "x":
        print("Saindo do sistema...")
        exit()
    else:
        print("Opção incorreta")
        main_user()


def logar_usuario():
    """Realiza o login do usuário e permite a escolha de contas."""
    while True:
        logar_cpf = input("CPF (ou /x para voltar)\n=> ")
        if logar_cpf == "/x":
            main_user()
            return
        logar_senha = input("Senha (ou /x para voltar)\n=> ")
        if logar_senha == "/x":
            main_user()
            return
        
        usuario_encontrado = None
        
        for usuario in usuarios:
            if usuario["cpf"] == logar_cpf and usuario["senha"] == logar_senha:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado:
            print('Contas disponíveis. Digite o número da conta que deseja acessar:')
            for idx, conta in enumerate(usuario_encontrado["contas"]):
                print(f"{idx + 1} - Agência: {conta['agencia']} - Saldo: R${conta['saldo_conta']:.2f}")
            conta_escolhida = input("\n=> ")
            if conta_escolhida == "/x":
                main_user()
                return
            conta_selecionada = usuario_encontrado["contas"][int(conta_escolhida) - 1]
            main(usuario_encontrado, conta_selecionada)
        else:
            print("CPF ou senha incorretos, tente novamente.")


# Inicializa o sistema
usuarios = []
main_user()
