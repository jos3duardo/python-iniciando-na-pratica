import getpass
import os

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


def main():
    header()
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        clear()
        header()
        print ('1 - Saldo')
        print ('2 - Saque')
        if accounts_list[account_typed]['admin']:
            print ('10 - Incluir cédulas')
        option_typed = input('escolha uma das opcoes acima: ')
        if option_typed == '1':
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a quantidade a ser incluido: ')
            # money_slips[mpney_bill_typed] = money_slips[amount_typed] + int(amount_typed)
            money_slips[money_bill_typed] += int(amount_typed)
            print (money_slips)
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')

            money_slips_user = {}
            value_int = int(value_typed)

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print ('O caixa não tem cédulas disponiveis para este valor')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                print ('Pegue as notas: ')
                print (money_slips_user)
    else:
        print ('\n!!!!!!!!!!  Conta invalida  !!!!!!!!!!!!\n')


# limpa a tela do terminal
def clear():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def header():
    print ('****************************************')
    print ('*********** Caixa Eletronico ***********')
    print ('****************************************')


# pausa do programa
def pause():
    input('Presione <ENTER> para continuar ...')


# enquanto o while for true o programa fica em execução
while True:
    main()
    pause()
    clear()

