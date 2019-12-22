import os


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