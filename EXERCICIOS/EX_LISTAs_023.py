from random import randint
from time import sleep

print('-=' * 30)
print(' >> PASSWORD GENERATOR M-SECURITY << '.center(60))
print('-=' * 30)
senha = []
sorteados = []
cont = 1
n = 0
n = int(input('Quantas senhas deseja gerar? '))
while cont <= n:
    sorteados.clear()
    sleep(0.8)
    print(f'Senha {cont}: ', end=' ')
    for c in range(0, 9):        
        while True:
            senha = randint(0, 100)
            if senha not in sorteados:
                sorteados.append(senha)               
                print(f'[{senha}]', end=' ')
                break  
    print()  
    cont = cont + 1
sleep(0.8)    
print('-=' * 30)
print(' - PROCESSO FINALIZADO! - '.center(60))
print('-=' * 30)