import utils
import operations
from file import load_bank_data
from bank_account_variables import money_slips


def main():
    load_bank_data()
    print(money_slips)
    utils.header()

    account_auth = operations.auth_account()

    if account_auth:
        utils.clear()
        utils.header()

        option_typed = operations.get_menu_options_typed(account_auth)
        operations.do_operation(option_typed, account_auth)
    else:
        print('\n!!!!!!!!!!  Conta invalida  !!!!!!!!!!!!\n')


# enquanto o while for true o programa fica em execução
while True:
    main()
    utils.pause()
    utils.clear()

