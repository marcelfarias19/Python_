#crie um programa que gerencie o aproveitamento de um jogador de futebol, o programa vai ler o nome do jogador e quantas partidas ele jogou, depois vai ler a quantidade gols feitos em cada partida, no final tudo isso será guardado em um dicionário, incluindo o total de gols feitos em dutante o campeonato.

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
gols = []
n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(n):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))   
    jogador['gols'] = gols
    
print('-='*30)
print(jogador)

