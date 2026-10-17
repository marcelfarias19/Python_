#faça um programa que leia um número e mostre seu fatorial.

num1= int(input('Digite o número que deseja o fatorial: '))
print()

cont = 1
fat = 1
while cont <= num1:
    fat = fat * cont    
    
    cont = cont + 1
    print('{} '.format(fat), end=' ')
   
print()
print('O fatorial de {} é {}!'.format(num1, fat))

