# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de vizualização de detalhes do aproveitamento de cada jogador.
jogador = {}
resp = 'N'
n = 0
gols = []
total = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))  
    n = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? ')) 
    for c in range(n):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = gols
    for gol in gols:
        total += gol   
    jogador['total'] = total
    resp = str(input('você deseja continuar? [S/N]')).upper().strip()
    print('-='*40)
    if resp == 'N':
        break
