# Faça um programa que tenha uma função chamada contador() que receba 3 parâmetros: ínico, fim e passo e realize a contagem.
# seu programa tem que realizar 3 contagens através da função criada.
# A - de 1 até 10, de 1 em 1
# B - de 10 ate 0, de 2 em 2
# C - uma contagem personalizada.

from time import sleep

def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)    
    if i < f:
       cont = i
       while cont <= f:
           print(f'{cont}', end=' ', flush=True)
           sleep(0.5)
           cont += p
       print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p 
        print('FIM!')           
             
def linha():
    print('-='*20)

linha()
contagem(1, 10, 1)
linha()
contagem(10, 0, 2)
linha
print('Agora é sua vez de personalizar a contagem')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
linha()