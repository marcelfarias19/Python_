#jogo de jokempô

import random
computador = random.randint(1, 3)
jogador = int(input('--Jokempô-- \n [1]Pedra \n [2] papel \n [3] Tesoura : \n'))
print('Jogador {} x Computador {}'.format(jogador, computador))

if jogador == 1 and computador == 2: 
    print('computador Venceu!')
elif jogador == 1 and computador == 3:
    print('Jogador venceu!')
elif jogador == 2 and computador == 3:
    print('Computador venceu!') 
elif jogador == 2 and computador == 1:
    print('Jogador venceu!')
elif jogador == 3 and computador == 1:
    print('Computador venceu!')
elif jogador == 3 and computador == 2:
    print('Jogador venceu!')
elif jogador == 1 and computador == 1:
    print('Empate')
elif jogador == 2 and computador == 2:
    print('Empate') 
elif jogador == 3 and computador == 3:
    print('Empate')

