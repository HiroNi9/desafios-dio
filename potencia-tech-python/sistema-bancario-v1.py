# Gabriel | HiroNi9
#
# Versão 1.0 do desafio do sistema bancário

# Variaveis do programa
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Menu das opções
menu = ("""
-----------------------        
Escolha uma das Opções
[D] Despositar
[E] Visualizar Extrato
[S] Sacar
[Q] Sair
-----------------------        
=>  """)

# Inicio do programa
print("""
Bem-vindo ao nosso novo sistema bancário""")
while True:
    # Estrutura condicional das funções do sistema
    opcao = input(menu).lstrip().lower()

    # Condição para a função "Depositar"
    if opcao[0] == "d":

        valor_deposito = float(input("Quanto deseja depositar? =>R$ "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito realizado de R${valor_deposito:,.2f}\n"

            print(f"\nVocê realizou um deposito de R${valor_deposito:,.2f}")
            print(f"Saldo atual => R${saldo:,.2f}")

        else: 
            print("Valor incorreto, tente novamente...")

    # Condição para a função "Sacar"
    elif opcao[0] == "s":
        valor_saque = float(input("Qual o valor que deseja sacar? => R$"))

        if (numero_saques == LIMITE_SAQUES):
            print("\nVocê utilizou o seu limite de saques diários, não é possível realizar mais saques.")
        elif (valor_saque > limite):
            print("\nO valor solicitado é maior que o valor limite disponível para saque, tente novamente.")
        elif (valor_saque > saldo):
            print("\nSaldo insuficiente, por favor, deposite mais fundos em sua conta ou saque um valor menor")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque realizado de R${valor_saque:,.2f}\n"
            numero_saques += 1

            print(f"\nVocê realizou um saque de R${valor_saque:,.2f}")
            print(f"Saldo atual => R${saldo:,.2f}")
        
        else:
            print("Valor incorreto, tente novamente...")



    # Condição para a função "Visulizar extrato"    
    elif opcao[0] == "e":
        print("=============Extrato=============")
        print("Não foi realizadas nenhuma movimentação na conta" if not extrato else extrato)
        print(f"Saldo na conta: R${saldo:,.2f}""")
        print("=" * 33)
        
    # Condição para sair do programa
    elif opcao[0] == "q": 
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    # Tratamento de erro de digitação
    else:
        print("Opção inválida, digite novamente!")