print('=' * 20)
print('CONVERSOR DE METROS')
print('=' * 20)

met = float(input('digite o valor em metros que deseja a conversão: '))
cen = met * 100
mil = met * 1000
print('A conversão do valor {} metros para centimetros é {:.3f} centimetros'.format(met, cen))
print('A conversao do valor {} metros para milimetros é {:.3f} milimetros'.format(met, mil))