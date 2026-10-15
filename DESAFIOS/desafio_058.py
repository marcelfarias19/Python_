#melhorar o jogo do desafio 028

import random 
computador = random.randint(0, 5)

jogador = 0
palpites = 0
while jogador != computador:
    
    jogador = int(input('Digite um número de 0 a 5 e veja se você adivinhou: ')) 
    
    if jogador != computador:    
        print('Errou! tente novamente')    
    
    palpites = palpites + 1      

print('Parabens!! você acertou \o/...')
print('Voce precisou de {} para acertar.'.format(palpites))
    