#Somadores de números primos

s = 0 
for cont in range(1, 500):
    if cont % 3 == 0:
        s += cont
         
print('A soma dos números ímpares que são multiplos de 3 entre 1 a 500 é {}'.format(s))