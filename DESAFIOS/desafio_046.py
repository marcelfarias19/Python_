#ccontagem regressiva

from time import sleep
print('Vai começar a contagem regressiva para os fogos.')

for cont in range(10, -1, - 1):
    sleep(1)
    print(cont)
print('Feliz ano novo!!')
    