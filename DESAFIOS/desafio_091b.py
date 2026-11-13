# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios, guarde esses resultados em um dicionário. no final coloque esse dicionário erdem, sabendo que o vencedor tirou o maior número do dado.
from random import randint
from time import sleep
from operator import itemgetter     # comando importante para botar na ordem
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)   
}
print('Valores sorteados: ')
print()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.8)
print()
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # comando exencial para esse Exercício  
print('Ranking dos jogadores')
print()
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar {v[0]} com {v[1]}')
    sleep(0.8)
