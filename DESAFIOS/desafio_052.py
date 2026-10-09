#Programa para saber se é um número é primo.

print('-- DESCOBRINDO NÚMEROS PRIMOS --')
p1 = int(input('Digite um valor: '))

primo = 0
contprimo = 0
for cont in range(1, p1):
    if p1 % cont == 0 :
        primo += cont
        contprimo = contprimo + 1 

print('-------------------')

print('O número {} foi divisivel {} vezes.'.format(p1, contprimo))    
   
if primo >= 3 :
    print('{} não é um número primo.'.format(p1))
else:
    print('{} é um número primo.'.format(p1))   
   
           
  
       