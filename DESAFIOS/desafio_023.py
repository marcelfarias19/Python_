#Fazer um programa que leia de 0 ate 9999.

num = input('digite um numero de 0 até 9999: ')
print('unidade: {} '.format(num[3:]))
print('dezenas: {}'.format(num[2:3]))
print('Centena: {}'.format(num[1:2]))
print('Milhar: {}'.format(num[0:1]))
