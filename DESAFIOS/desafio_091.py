# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios, guarde esses resultados em um dicionário. no final coloque esse dicionário erdem, sabendo que o vencedor tirou o maior número do dado.

from random import randint
from time import sleep 
from operator import itemgetter
jogador = {}
print('VALORES SORTEADOS:')
for c in range(1, 5):           
    sleep(0.6)  
    dado = randint(1, 100)    
    print(f'   O jogador {c} tirou {dado}')
    jogador[c] = dado    
print()

ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    sleep(0.6)
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}')
   

 
