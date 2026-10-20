# Jogo de par ou ímpar.

from random import randint
computador = randint(1, 10)
par = 0
impar = 0
while True:
    print('=-'*15)
    print('--JOGO DE PAR OU ÍMPAR--')
    print('=-'*15)
    
    jogador = int(input('Diga um valor: '))
    game = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    result = jogador + computador
    
    print(f'Você jogou {jogador} o computador jogou {computador}.Total de {result}')
        
    if result % 2 == 0 and game == 'P':
        print(f'{result} é Par')
        print(f'Game over! Você venceu {par} vezes')
        par = par + 1
        break
    elif result % 2 == 1 and game == 'I': 
        print(f'{result} é ímpar')
        print(f'Game over! Você venceu {impar} vezes')
        impar = impar + 1
        break
    else:
        print('Você Perdeu!')    
   

