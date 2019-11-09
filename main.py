import getpass

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
            'value': 1500
        },
        '0002-02': {
            'password': '123456',
            'name': 'Fulada de tal',
            'value': 2000
        }
    }

    if  account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        print ('****************************************')
        print ('*********** Caixa Eletronico ***********')
        print ('****************************************')
        print ('1 - saldo')
        option_typed = input ('escolha uma das opcoes acima: ')
        if option_typed == '1':
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])

    else:
        print ('\n!!!!!!!!!!  Conta invalida  !!!!!!!!!!!!\n')
