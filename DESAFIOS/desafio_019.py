import random
alun1 = str(input('Primeiro aluno: '))
alun2 = str(input('Segundo aluno: '))
alun3 = str(input('terceiro aluno: '))
alun4 = str(input('quarto aluno: '))
lista = [alun1, alun2, alun3, alun4]
escolhido = random.choice(lista)
print('O nome do escolhido foi {}'.format(escolhido))