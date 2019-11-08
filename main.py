import getpass

print ('****************************************')
print ('*********** Caixa Eletronico ***********')
print ('****************************************')
account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')
print (account_typed)
print (password_typed)

accounts_list = {
    '0001-02': {
        'password': '123456',
        'name': 'Fuladno da Silva',
        'value': 0
    },
    '0002-02': {
        'password': '123456',
        'name': 'Fulada de tal',
        'value': 0
    }
}

if  account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
    print('Conta valida')
else:
    print ('Conta invalida')
