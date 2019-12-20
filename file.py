import os
from bank_account_variables import money_slips


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


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)