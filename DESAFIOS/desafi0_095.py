# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de vizualização de detalhes do aproveitamento de cada jogador.
jogador = {}
resp = 'N'
n = 0
lista = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))  
    n = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? ')) 
    gols = []
    for c in range(n):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = gols
    total = 0
    for gol in gols:
        total += gol   
    jogador['total'] = total
    lista.append(jogador.copy())
    resp = str(input('você deseja continuar? [S/N]')).upper().strip()
    print('-='*30)
    if resp == 'N':
        break
print('COD NOME:           GOLS:           TOTAL:')
for i, v in enumerate(lista):
    print(f' {i:<2} {v["nome"]:<14} {v["gols"]}            {v["total"]}')
print('-='*30)
cont = 0
while cont != 999:
    cont = int(input('Mostrar dados de qual jogador? (999 o programa para)'))
    for i, c in enumerate(lista): 
        if cont == i:
            print(f'-- LEVENTAMENTO DO JOGADOR {c["nome"]}')
            for i, g in enumerate(c["gols"]):
                print(f'No jogo {i} fez {g} gols.')          
print('')
print('>> ENCERRADO <<')
            
    