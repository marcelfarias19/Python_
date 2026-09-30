#descobrfir se o ano é bissexto

ano = int(input('Para descobrir se o ano é bissexto digite o ano: '))

if ano % 400 == 0:
    print('{} é ano Bissexto.'.format(ano))
else:
    print('{} não é ano bissexto.'.format(ano))
    