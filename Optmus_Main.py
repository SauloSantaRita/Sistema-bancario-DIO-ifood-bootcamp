import textwrap

def menu():
    menu = """\n
    ================= MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
          saldo += valor
          extrato += f'Deposito:\tR$ {valor: .2f}\n'
          print("\n**** Depósito realizado com sucesso ! ****")
    else:
          print("\n !!!! Operação falhou! O valor informado é inválido. Tente novamente !!!!")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, qtde_saques, limite_saques):
    if valor <= 0:
        print('!!!! Valor digitado inválido para saque !!!!')

       # verificar se o saque é maior que o saldo 
    elif valor > saldo:
        print(f'!!!! Saldo insuficiente ! Saldo atual: R$ {saldo:.2f} !!!!')

       # verificar se o saque é maior que o limite de saque 
    elif valor > limite:
        print(f'!!!! Limite de R$ {limite:.2f} excedido !!!!')

       # verificar se a quantidade de saques excedeu o limite 
    elif qtde_saques >= limite_saques:
        print(f'!!!! Quantidade de saques excedida, quantidade máxima permitida é de {limite_saques} saques !!!!')

       # caso cumpra todos os requisitos, realizar o saque do saldo atual 
    else:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        qtde_saques += 1
        print('**** Saque realizado com sucesso ! ****')

    return saldo, extrato


def exibir_extrato(saldo, / , *, extrato):
      print('\n---------------------------------')
      print('********** EXTRATO **************')
      print('\nSem Movimentação !' if not extrato else extrato)
      print(f'\nSaldo atual:\tR$ {saldo:.2f}')
      print('=================================')


def filtrar_usuarios(cpf, usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None


def cadastrar_usuario(usuarios):
      cpf = input("Informe o CPF (digitar somente os números): ")
      usuario = filtrar_usuarios(cpf, usuarios)

      if usuario:
            print("\n!!!! CPF já cadastrado !!!!")
            return
      
      nome = input("Informe o nome completo do usuário: ")
      data_nascimento = input("Informe a data de nascimento no formato dd-mm-aaaa: ")
      endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/UF): ")

      usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
      print("**** Usuário cadastrado com sucesso ! ****")


def cadastrar_conta(agencia, numero_conta, usuarios):
      cpf = input("Informe o CPF (digitar somente os números): ")
      usuario = filtrar_usuarios(cpf, usuarios)

      if usuario:
            print("\n**** Parabéns ! Você cadastrou sua conta ! ****")
            return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
      
      print("\n!!!! Usuário não encontrado, favor cadastrar o usuáiro no menu de opções !!!!")


def listar_contas(contas):
      for conta in contas:
            linha = f"""
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 50)
            print(textwrap.dedent(linha))


def main():
      AGENCIA = "0001"
      usuarios = []
      contas = []

      extrato = ""
      saldo = 0
      limite = 500
      qtde_saques = 0
      LIMITE_SAQUES = 3

      while True:
            opcao = menu()

            if opcao == 'd':
                valor = float(input('Digite o valor do depósito: '))

                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == 's':
                valor = float(input('Digite o valor do saque: '))

                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, qtde_saques=qtde_saques, limite_saques=LIMITE_SAQUES)
            
            elif opcao == 'e':
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == 'nu':
                cadastrar_usuario(usuarios)

            elif opcao == 'nc':
                numero_conta = len(contas) + 1
                conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                     contas.append(conta)

            elif opcao == 'lc':
                listar_contas(contas)

            elif opcao == 'q':
                print('Sistema encerrado, obrigado por utilizar nosso terminal')
                break

            else:
                print('Opção digitada inválida, por favor tente novamente !') 


main()