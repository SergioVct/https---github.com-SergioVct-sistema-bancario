print('''
      ***********************
      *                     *
      *      Bem vindo      *
      *                     *
      ***********************''')
menu = '''
    [1] deposito
    [2] saque
    [3] Extrato
    [4] sair
'''

saldo = 500.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"foi depositado R$ {valor}\n"
    elif opcao == "2":
        if LIMITE_SAQUES > 0:
            valor = float(input("digite o valor a sacar: "))
            if valor < 501:
                saldo -= valor
                extrato += f"foi sacado R$ {valor}\n"
                LIMITE_SAQUES -= 1
                print(f"foi sacado R$ {valor}")
                print(f"limite restante para saque diario: {LIMITE_SAQUES}") 
            elif valor > 500:
                print("valor excede seu limite por saque")

        else:
            continue
    elif opcao == "3":
        print(f"seu saldo é de R$ {saldo}")
        print(extrato)
    else :
        break
        