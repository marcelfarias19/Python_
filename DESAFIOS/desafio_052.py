#Programa para saber se é um número é primo.

print('-- DESCOBRINDO NÚMEROS PRIMOS --')
p1 = int(input('Digite um valor: '))

for cont in range(1, p1 + 1):
    if p1 % cont == 0 and p1 % p1 == 0:
        primo = p1
        print('{} é divisivel por 1 e por ele {}'.format(primo, cont))
    else:
        print('não é um número primo')
        
        
    


    
     
