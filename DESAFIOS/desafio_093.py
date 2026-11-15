#crie um programa que gerencie o aproveitamento de um jogador de futebol, o programa vai ler o nome do jogador e quantas partidas ele jogou, depois vai ler a quantidade gols feitos em cada partida, no final tudo isso será guardado em um dicionário, incluindo o total de gols feitos em dutante o campeonato.

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
gols = []
total = 0
n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(n):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))   
    jogador['gols'] = gols
for v in gols: # eu poderia usar aqui o método sum.
    total += v 
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {n} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]}')