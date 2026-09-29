#faça um programa que leia 

nome = input('Digite o nome completo: ')
parte = nome.split()
print('Primeiro nome: {}'.format(parte[0]))
print('segundo nome: {}'.format(parte[-1]))