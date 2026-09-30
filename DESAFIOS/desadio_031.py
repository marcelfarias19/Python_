#cobrador de passagem

dist = int(input('Digite a distância em km de sua viagem: '))

if dist > 200:
    ticket = float(dist * 0.50)
    print('Sua passagem custará R$ {:.2f}'.format(ticket))
else:
    ticket = float(dist * 0.45)
    print('Sua passagem custará R$ {:.2f}'.format(ticket))
    