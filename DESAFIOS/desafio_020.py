import random
alun1 = str(input('primeiro aluno: '))
alun2 = str(input('Segundo aluno: '))
alun3 = str(input('Terceiro aluno: '))
alun4 = str(input('Quarto aluno: '))
ordem = [alun1, alun2, alun3, alun4]
random.shuffle(ordem)
print('A ordem do sorteio da apresentação é {}'.format(ordem))