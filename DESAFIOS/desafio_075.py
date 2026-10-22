# Desenvolver um programa que leia 4 valores e guardeos em uma tupla.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

e = (a, b, c, d)
    
print(f'Você digitou os valore {e}')
val_09 = 0
if e[0] == 9:
    val_09 += 1 
if e[1] == 9:
    val_09 += 1
if e[2] == 9:
    val_09 += 1
if e[3] == 9:
    val_09 += 1
print(f'O valor 9 apareceu {val_09} vezes')
    
pos = 0
if 3 in e:             # prestar mais tenção onde pode ser usado a condição in no if / ex: if 3 in e
    pos = e.index(3)
    print(f'o valor 3 aparece na {pos + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
    
pares = []              # tive que criar uma lista que ainda não apareceu em aula
if e[0] % 2 == 0:
    pares.append(e[0])    # coloquei um método que ainda não foi apresentado em aula / .append(lista)
if e[1] % 2 == 0:
    pares.append(e[1])
if e[2] % 2 == 0:
    pares.append(e[2])
if e[3] % 2 == 0:
    pares.append(e[3]) 
     
print(f'Os valores pares digitados foram {pares}')