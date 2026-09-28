print('=' * 20)
print('QUANTIFICADOR DE TINTA')
print('=' * 20)

larg = float(input('Digite po valor da largura: '))
alt = float(input('Digite o valor da altura '))
parede = larg * alt
ltinta = parede / 2
print('A área da parede de {:.2f} M² vai precisar de {:.2f} litros de tinta'.format(parede, ltinta)) 
