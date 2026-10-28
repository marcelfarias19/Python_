# Temperatura da semana / crie um programa que leia 5 temperaturas e guarde todas em uma lista.
# O programa deverá:
# 1 - Mostrar todas as temperaturas digitadas.
# 2 - identificar a maior temperatura e guarde registrada.
# 3 - Mostrar a posição em que a maior temperatura apareceu.
# 4 - identificar a menor temperatura registrada.
# 5 - Mosrtar a posição em que a menor temperatura apareceu.
# 6 - se a maior temperatura aparecer mais de uma vez, mostrar todas as posições.

temperatura = []
maior = 0
menor = 0

for cont in range(0, 5):
    n = int(input(f'Digite a temperatura na posição {cont}: '))
    temperatura.append(n)
    
    if cont == 0:
        maior = menor = temperatura[cont]
    if temperatura[cont] > maior:
        maior = temperatura[cont] 
    if temperatura[cont] < menor:
        menor = temperatura[cont]
        
print('-='*20)
print(f'As temperaturas registradas foram {temperatura}')
print(f'A maior temperatura foi de {maior} na posição', end=' ')
for i, v in enumerate(temperatura):
    if v == maior:
        print(f'{i}...', end=' ')
print() 
print(f'A menor temperatura {menor} na posição', end=' ')
for i, v in enumerate(temperatura):
    if v == menor:
        print(f'{i}...', end=' ')
    
    

