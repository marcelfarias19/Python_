# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios, guarde esses resultados em um dicionário. no final coloque esse dicionário erdem, sabendo que o vencedor tirou o maior número do dado.

from random import randint
from time import sleep 
jogador = {}
print('Valores sorteados:')
for c in range(1, 5):           
    sleep(0.6)  
    dado = randint(1, 100)    
    print(f'O jogador {c} tirou {dado}')
    jogador[c] = dado    

print()
print('Ranking dos jogadores:')
pont = 0
ind = 0 
classificados = []
cont = 1
while cont <= len(jogador):
    pont = 0            
    for i, v in jogador.items():       
        if i not in classificados and v > pont:
            pont = v
            ind = i     
    classificados.append((ind, pont))  
    print(f'{cont} {ind} {pont}')        
    cont = cont + 1   
