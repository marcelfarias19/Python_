from random import randint
from time import sleep
 
print('=-'*30)
print('>> SORTEIO MEGA-SENA <<'.center(60))
print('=-'*30)

cont = 1
num = []
sorteados = []
n = int(input('Quantos jogos Você quer? '))
while cont <= n: 
    sorteados.clear()   
    sleep(0.8)
    print(f'Jogo {cont}: ', end=' ')
    for c in range(0, 6):
        while True: 
            num = randint(1, 60)                       
            if num not in sorteados:
                sorteados.append(num)                                
                print(f'{num}', end=' ')
                break
    print()    
    cont = cont + 1
    
print('-='*30)
sleep(0.8)
print('FINALIZADO!')