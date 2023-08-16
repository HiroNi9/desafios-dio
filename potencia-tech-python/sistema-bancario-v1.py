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
        print(opcao)

    # Condição para a função "Visulizar extrato"    
    elif opcao[0] == "e":
        print(opcao)
    
    # Condição para a função "Sacar"
    elif opcao[0] == "s":
        print(opcao)
        
    # Condição para sair do programa
    elif opcao[0] == "q": 
        break

    # Tratamento de erro de digitação
    else:
        print("Opção inválida, digite novamente!")