#programa que le o ano de nascimento e fala se é hora de se alistar.
anoatual = int(input('Digite o ano atual: '))
ano = int(input('digite o ano so seu nascimento: '))
alistar = anoatual - ano

if alistar < 18:
    sold = 18 - alistar
    print('falta {} anos para seu alistamento.'.format(sold))
elif alistar == 18:
    print('É hora de se alistar.')
elif alistar > 18:
    sold = alistar - 18
    print('Seu prazo para se alistar já passou {} anos.'.format(sold))





