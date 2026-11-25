# faça um programa que tenha uma função chamda maior(), que receba vários parâmetros com valores inteiros.
# seu programa tem que analisar todos os valores e dizer qual é o maior.
from time import sleep

def linha():
    print('-='*20)
    
def contador(*num):
    print('Analisando valores passados...')
    for v in num:
        print(f'{v}', end=' ', flush=True )
        sleep(0.6)
    print(f'foram informados {len(num)} ao todo', end=' ') 
    maior_num = num[0]
    print()
    for v in num:
        if v > maior_num:
            maior_num = v
    print(f'O maior valor informado foi {maior_num}')
       

linha()        
contador(2, 3, 9, 1) 
linha()  
contador(9, 23, 4, 56, 99)  
linha() 
contador(23, 26, 98, 77, 84, 125, 10 )
linha()