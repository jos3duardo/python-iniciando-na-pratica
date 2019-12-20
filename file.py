import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

print(BASE_PATH)

file = open(BASE_PATH + '/_file_teste.dat', 'w')
file.write('Teste de escrita em arquivo')
file.write('\n')
file.write('Teste de escrita em arquivo')
file.close()