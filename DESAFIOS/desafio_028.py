#jogo do adivinha
import random
num = random.randint(0, 5) 
esc = int(input('digite um numero de 0 a 5 e veja se você adivinhou: '))

if esc == num:
    print('Parabéns você acertou {}!'.format(num))
else:    
    print('infelizmente você não acertou, tente de novo!')
print('--FIM--')