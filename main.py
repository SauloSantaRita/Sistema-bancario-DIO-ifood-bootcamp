
# criar o menu de opções
menu = '''
Selecione uma opção de operação:

[d] - Realizar um Depósito
[s] - Realizar um Saque
[e] - Visualizar o Extrato
[q] - Sair

=>'''

extrato = ''
saldo = 0
LIMITE = 500
qtde_saques = 0
LIMITE_SAQUES = 3

while True:

      
   # mostrar o menu e atribuir uma das opções
   opcao = input(menu)

   # opção de depósito 
   if opcao == 'd':
      valor = float(input('Digite o valor do depósito: '))
      
      # verificar se o valor de depósito é positivo  
      if valor > 0:
         saldo += valor
         extrato += f'Depósito: {valor:.2f}\n'
         print('Depósito realizado com sucesso !')
      # mensagem de valor negativo   
      else:
         print('Valor digitado inválido para depósito')

   # opção de saque     
   elif opcao == 's':
       saque = float(input('Digite o valor do saque: '))

       # verificar se o saque é negativo 
       if saque <= 0:
           print('Valor digitado inválido para saque')

       # verificar se o saque é maior que o saldo 
       elif saque > saldo:
           print(f'Saldo insuficiente ! Saldo atual: R$ {saldo:.2f}')

       # verificar se o saque é maior que o limite de saque 
       elif saque > LIMITE:
           print(f'Limite de R$ {LIMITE:.2f} excedido !')

       # verificar se a quantidade de saques excedeu o limite 
       elif qtde_saques >= LIMITE_SAQUES:
           print(f'Quantidade de saques excedida, quantidade máxima permitida é de {LIMITE_SAQUES} saques !')

       # caso cumpra todos os requisitos, realizar o saque do saldo atual 
       else:
           saldo -= saque
           extrato += f'Saque: {saque:.2f}\n'
           qtde_saques += 1
           print('Saque realizado com sucesso !')

   # opção de visualizar o extrato
   elif opcao == 'e':
       print('\n---------------------------------')
       print('********** EXTRATO **************')
       print('\nSem Movimentação !' if not extrato else extrato)
       print(f'\nSaldo atual: R$ {saldo:.2f}')
       print('=================================')
    
   # sair do sistema 
   elif opcao == 'q':
        print('Sistema encerrado, obrigado por utilizar nosso terminal')
        break    

   else:
       print('Opção digitada inválida, por favor tente novamente !')