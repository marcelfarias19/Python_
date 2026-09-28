import math 
angulo = int(input('Digite o valor do angulo: ' ))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do angulo {} em seno é {:.2f} em cosseno é {:.2f} e em tangente {:.2f}.'.format(angulo, seno, cosseno, tangente))


