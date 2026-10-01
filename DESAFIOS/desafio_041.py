#confederação de natação
anoatual = int(input('Digite o ano atual: '))
anoatleta = int(input('Digite o ano do nascimento do atleta: '))
categoria = anoatual - anoatleta

if categoria <= 9:
    print('idade {} / O atleta é Mirim.'.format(categoria))
elif categoria >= 10 and categoria <= 14:
    print('idade {} / O atleta é Infantil.'.format(categoria))
elif categoria >= 19 and categoria <= 20:
    print('idade {} /  O atleta é Junior.'.format(categoria))
elif categoria > 20:
    print('idade {} / O atleta é Master.'.format(categoria))
