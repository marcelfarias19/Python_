import random
from time import sleep
computador = random.randint(0, 2)
jogador = int(input(''''--Jokempô--
escolha entre as opções.
[0] Pedra
[1] Papel
[2] tesoura'''))

print('Jo')
sleep(1)
print('kem')
sleep(1)
print('pô')
sleep(1)

print('O jogador escolheu {}'.format(jogador))
print('O computador escolheu {}'.format(computador))

if computador == 0:
    if jogador == 0:
        print('Jogo empatado')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
        print('jogo empatado')
    elif jogador == 2:
        print('joagador venceu')
    else:
        print('jogada inválida')
elif computador == 2 :
    if jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('compuatdor venceu')
    elif jogador == 2:
        print('jogada empatada')
    else:
        print('jogada inválida')