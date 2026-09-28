import math
cateto_adjacente = float(input('digite o o valor do angulo do cateto adjacente: '))
cateto_oposto = float(input('Digite o valor do angulo do cateto oposto: '))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto) 
print('o valor do primeiro cateto {} e do segundo cateto {} resultam na hipotenusa {:.2f}'.format(cateto_adjacente, cateto_oposto, hipotenusa)) 
