# 
#? Menu onde mostra as opções que podem ser executadas no sistema bancário
menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair do sistema

"""

#? Variáveis declaradas que serão usadas
saldo= 0
limite= 500
extrato= ""
numero_saques = 1
LIMITE_SAQUES = 3

#? Laço de repetição while para que o sistema continue executando enquanto o usuário quiser
while True:

    opção= input(menu)

    if opção == 'd': #? Opção para o usuário depositar um valor em sua conta
        valor = float(input('Quanto deseja depositar? R$'))

        if valor > 0: #? Quando o valor de depósito é escolhido, o sistema soma esse valor ao saldo atual e adiciona essa operação no extrato
            saldo += valor
            extrato = f"Depósito: R$ {valor:.2f}\n"

        else: #? Caso ele informe o valor 0 ou um valor negativo, a operação falha
            print("Operação falhou! O valor informado é inválido.")

    elif opção == 's': #? Opção para o usuário sacar um valor de sua conta
        valor = float(input('Quanto deseja sacar? R$'))

        execedeu_saldo = valor > saldo 

        execedeu_limite = valor > limite

        execedeu_saques = numero_saques > LIMITE_SAQUES
        
        if execedeu_saldo: #? Caso o valor a sacar seja maior que o saldo atual da conta, a operação falha
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif execedeu_limite: #? Caso o valor seja maior que o limite de saque, a operação falha
            print("Operação falhou! Valor do saque execede o valor do limite.")

        elif execedeu_saques: #? Caso o número de saques diários seja maior que o limite de saques diários (Que é 3), a operação falha
            print("Operação falhou! Número máximo de saques atingido.")

        elif valor > 0: #? Quando o valor de saque é escolhido, o sistema subtrai esse valor do saldo atual, adiciona a operação no extrato e conta como 1 saque diário
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else: #? Se o valor a sacar for 0 ou negativo, a operação falha
            print("Operação falhou! O valor informado é inválido.")
        
    elif opção == "e": #? Nessa opção o extrato é exibido para o usuário, com todas as operações realizadas por ele no dia

        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas transações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("="*40)        
        
    elif opção == 'q':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
print("Obrigado por usar nosso sistema bancário. Volte sempre!!")