def verificar_saldo(saldo):
    print(f"Saldo disponível: R$ {saldo:.2f}")

def realizar_deposito(saldo, limite_diario_deposito, extrato):
    valor_deposito = float(input("Insira o valor a depositar: "))
    if valor_deposito > limite_diario_deposito:
        print("Erro: Valor excede o limite diário de depósito.")
    elif valor_deposito <= 0:
        print("Valor inválido!")
    else:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito realizado. Novo saldo: R$ {saldo:.2f}")
    return saldo, extrato

def realizar_saque(saldo, limite_diario_saque, extrato):
    valor_saque = float(input("Insira o valor de saque: "))
    if valor_saque > saldo:
        print("Erro: Saldo Insuficiente.")
    elif valor_saque > limite_diario_saque:
        print("Erro: Valor excede o limite diário de saque.")
    elif valor_saque <=0:
        print("Valor inválido!")
    else:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        print(f"Saque realizado com sucesso. Novo saldo: R$ {saldo:.2f}")
    return saldo, extrato



print("Bem vindo ao Crutt Bank!")


#simulação de dados de conta
numero_da_conta = 2350
senha_da_conta = 2023
saldo = 20000
extrato = ""
limite_diario_deposito = 15000
limite_diario_saque = 10000
nome = "João"

while True:
    conta = int(input("Por favor, insira o número da sua conta: "))
    senha = int(input("Insira sua senha: "))

    if conta == numero_da_conta and senha == senha_da_conta:
        print(f"Olá {nome}, o que você deseja realizar hoje?")
        print()

        while True:
            opcao = input("Escolha uma opção:\n1- Verificar saldo da conta\n2- Depósito\n3- Saque\n4- Extrato\n0- Sair\n")

            if opcao == "1":
                verificar_saldo(saldo)
            elif opcao == "2":
                saldo, extrato = realizar_deposito(saldo, limite_diario_deposito, extrato)
            elif opcao == "3":
                saldo, extrato = realizar_saque(saldo, limite_diario_saque, extrato)
            elif opcao == "4":
                print(extrato)
            elif opcao == "0":
                print("Obrigado por utilizar o Crutt Bank. Até a próxima")
                exit()
            else:
                print("Opção inválida.")
            print()

    else:
        print("Conta ou senha inválida")
        

