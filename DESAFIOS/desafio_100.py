# faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). a primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela fujnção anterior.

from random import randint
from time import sleep

def sorteados(lst):
    print(f'sorteando {len(lst)} valores da lista: ', end=' ')
    for v in lst:
        print(f'{v},', end=' ', flush=True)
        sleep(0.6)
    print('Pronto!')  
    
def somaPar(lst):
    soma_par = 0
    for v in lst:
        if v % 2 == 0:
            soma_par += v
    print(f'somando os valores de {lst}, temos {soma_par}')

numeros = [randint(1, 10), randint(1,10), randint(1, 10), randint(1, 10), randint(1, 10)] 

sorteados(numeros)
somaPar(numeros)