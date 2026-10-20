# Jogo de par ou ímpar.

from random import randint
computador = randint(1, 100)
vit = 0
while True:
    print('=-'*15)
    print('--JOGO DE PAR OU ÍMPAR--')
    print('=-'*15)
    
    jogador = int(input('Diga um valor: '))
    game = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    result = jogador + computador
    
    print(f'Você jogou {jogador} o computador jogou {computador}.Total de {result}')
        
    if result % 2 == 0 and game == 'P':
        print(f'{result} é Par você ganhou')
        print('Vamos jogar novamente')        
        vit = vit + 1
        
    elif result % 2 == 1 and game == 'I': 
        print(f'{result} é ímpar você ganhou')
        print('Vamos jogar novamente')
        vit = vit + 1
     
    else:        
        print('VOCÊ PERDEU!')
        print(F'Game Over! Você venceu {vit}!')
        break
          
   

