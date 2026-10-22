# Exercícios de tuplas (reforço)

from random import randint

a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10 )
d = randint(0, 10) 
e = randint(0, 10)

n = (a, b, c, d, e)
maior_valor = n[0]
menor_valor = n[0]

print(f'os valores sorteados foram: {n} ')

if n[0] > maior_valor:
    maior_valor = n[0]
if n[1] > maior_valor:
    maior_valor = n[1] 
if n[2] > maior_valor:
    maior_valor = n[2]
if n[3] > maior_valor:
    maior_valor = n[3]
if n[4] > maior_valor:
    maior_valor = n[4]
    
if n[0] < menor_valor:
    menor_valor = n[0]
if n[1] < menor_valor:
    menor_valor = n[1]
if n[2] < menor_valor:
    menor_valor = n[2]
if n[3] < menor_valor:
    menor_valor = n[3]
if n[4] < menor_valor:
    menor_valor = n[4]

print(f'O maior valor sorteado foi {maior_valor}')
print(f'O menor valor sorteado foi {menor_valor}')