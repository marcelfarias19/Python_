# crie um programa que leia 5 preços de produtos e armazene em uma lista.
# o programa deverá:
# 1 - mostrar todos os preços digitados.
# 2 - identificar o maior preço.
# 3 - mostrar todas as posições.
# 4 - identificar o menor preço.
# 5 - Mostrar todas as posições que o menor preço aparece.

precos = [] 
maior = 0
menor = 0

for cont in range(0, 5):
    n = float(input(f'Digite o preço na posição {cont}: R$ '))
    precos.append(n)
    
    if cont == 0:
        maior = menor = precos[cont]
    if precos[cont] > maior:
        maior = precos[cont]
    if precos[cont] < menor:
        menor = precos[cont]        
print()
print('-='*20)
print(f'Os preços registrados foram {precos}')
print(f'O maior preço foi R$ {maior:.2f} na posição', end=' ')
for i, v in enumerate(precos):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor preço foi R$ {menor:.2f} na posição', end=' ')
for i, v in enumerate(precos):
    if v == menor:
        print(f'{i}...', end=' ')
print()

        