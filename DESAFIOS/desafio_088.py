# faça um programa quer ajude um jogador da mega sena a criar palpites, o programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
 
print('=-'*30)
print('>> SORTEIO MEGA-SENA <<'.center(60))
print('=-'*30)

lista = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60
]

cont = 1
n = int(input('Quantos jogos Você quer? '))
while cont <= n:
    sleep(0.8)
    print(f'Jogo {cont}: ', end=' ')
    for c in range(0, 6):
        lista = randint(1,61)                       
        print(f'[{lista}]', end=' ')
    print()    
    cont = cont + 1
        
    