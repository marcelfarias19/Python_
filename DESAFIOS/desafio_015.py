alug = int(input('Quantos dias alugados: '))
km = float(input('Quantos quilomêtros eu rodei: '))
tot1 = alug * 60
tot2 = km * 0.15
res = tot1 + tot2 
print('O total a pagar é de R${:.2f}'.format(res))