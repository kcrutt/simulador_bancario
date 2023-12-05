def verificar_saldo(saldo):
    print(f"Saldo disponível: R$ {saldo:.2f}")

def realizar_deposito(saldo, limite_diario):
    valor_deposito = float(input("Insira o valor a depositar: "))
    if valor_deposito > limite_diario:
        print("Erro: Valor excede o limite diário de depósito.")
    else:
        saldo += valor_deposito
        print(f"Depósito realizado. Novo saldo: R$ {saldo:.2f}")

def realizar_saque(saldo, limite_diario):
    valor_saque = float(input("Insira o valor de saque: "))
    if valor_saque > saldo:
        print("Erro: Saldo Insuficiente.")
    elif valor_saque > limite_diario:
        print("Erro: Valor excede o limite diário de saque.")
    else:
        saldo -= valor_saque
        print(f"Saque realizado com sucesso. Novo saldo: R$ {saldo:.2f}")



print("Bem vindo ao Crutt Bank!")

#simulação de dados de conta
numero_da_conta = 20380
senha_da_conta = 1304
saldo = 20000
limite_diario = 15000
limite_noturno = 5000
nome = "Fernando"
idade = 23

while True:
    conta = int(input("Por favor, insira o número da sua conta: "))
    senha = int(input("Insira sua senha: "))

    if conta == numero_da_conta and senha == senha_da_conta:
        print(f"Olá {nome}, o que você deseja realizar hoje?")
        print()

        while True:
            opcao = input("Escolha uma opção:\n1- Verificar saldo da conta\n2- Depósito\n3- Saque\n4- Sair\n")

            if opcao == "1":
                verificar_saldo(saldo)
            elif opcao == "2":
                realizar_deposito(saldo, limite_diario)
            elif opcao == "3":
                realizar_saque(saldo, limite_diario)
            elif opcao == "4":
                print("Obrigado por utilizar o Crutt Bank. Até a próxima")
                exit()
            else:
                print("Opção inválida.")
            print()

    else:
        print("Conta ou senha inválida")
        

