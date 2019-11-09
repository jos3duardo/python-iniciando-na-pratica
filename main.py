import getpass
import os

# enquanto o while for true o programa fica em execução
while True:
    print ('****************************************')
    print ('*********** Caixa Eletronico ***********')
    print ('****************************************')
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    accounts_list = {
        '0001-02': {
            'password': '123456',
            'name': 'Fuladno da Silva',
            'value': 1500,
            'admin': False
        },
        '0002-02': {
            'password': '123456',
            'name': 'Fulada de tal',
            'value': 2000,
            'admin': False
        },
        '1111-11': {
            'password': '123456',
            'name': 'Admin da Silva',
            'value': 2000,
            'admin': True
        }
    }
    money_slips = {
        '20': 5,
        '50': 5,
        '100': 5,
    }

    if  account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        # limpa a tela do terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        print ('****************************************')
        print ('*********** Caixa Eletronico ***********')
        print ('****************************************')
        print ('1 - Saldo')
        if accounts_list[account_typed]['admin']:
            print ('10 - Incluir cédulas')
        option_typed = input ('escolha uma das opcoes acima: ')
        if option_typed == '1':
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amount_typed = input('Digite a quantidade de cédulas: ')
            mpney_bill_typed = input('Digite a quantidade a ser incluido: ')
            money_slips[amount_typed] += int(amount_typed)
            print ('incluir cédulas')

    else:
        print ('\n!!!!!!!!!!  Conta invalida  !!!!!!!!!!!!\n')

    input('Presione <ENTER> para continuar ...')

    # limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')
