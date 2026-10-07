#Programa para saber se é um número é primo.

print('-- DESCOBRINDO NÚMEROS PRIMOS --')
p1 = int(input('Digite um valor: '))

primo = 0
for cont in range(1, p1):
    if p1 % cont == 0 and p1 % p1 == 0:
       primo += cont

print('-------------------')
       
if primo > 2 :
    print('{} não é um número primo.'.format(p1))
else:
    print('{} é um número primo.'.format(p1))   
   
           
  
       