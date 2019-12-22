import os
from bank_account_variables import money_slips, accounts_list


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

# file = open(BASE_PATH + '/_file_teste.dat', 'w')
# file.write('Teste de escrita em arquivo')
# file.write('\n')
# file.write('Teste de escrita em arquivo')
# file.close()


def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)


def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')


def write_bank_accounts(file):
    for account, account_data in accounts_list.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';'
            '\n'
        ))


def read_money_slips(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        money_bill_value = line[0:semicolon_pos]
        set_money_bill_value(money_bill_value)
        # 20=5000;50=50000
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos+1:len(line)]


def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=') # 20=5000
    money_bill = money_bill_value[0:equal_pos]
    count_money_bill_value = len(money_bill_value)
    value = money_bill_value[equal_pos + 1:count_money_bill_value]
    print(money_bill, value)
    money_slips[money_bill] = int(value)


def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)


def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';')
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        # 20=5000;50=50000
        if semicolon_pos + 1 == len(account_line):
            break
        else:
            account_line = account_line[semicolon_pos + 1:len(account_line)]
    add_bank_account(account_data)

def add_bank_account(account_data):
    accounts_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': True if account_data[4] == 'True' else 'False',
    }

def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()
    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()


def delete_file():
    file = open(BASE_PATH + '/_file_to_delete.dat', 'w')
    file.close()
    os.unlink(BASE_PATH + '/_file_to_delete.dat')
