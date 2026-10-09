# exercicio para treinar o in: ver se o valor esta dentro de uma coleção de dados.

frutas = ['maçã', 'banana', 'uva', 'laranja']

us_fruta = str(input('digite o nome de uma fruta: ')).strip()
if us_fruta in frutas:
    print('{} esta na lista'.format(us_fruta))
else:
    print('{} não está na lista'.format(us_fruta))
