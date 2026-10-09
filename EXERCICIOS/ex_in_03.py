# exercicio para treinar o in: ver se o valor esta dentro de uma coleção de dados.

artistas = ['racionais', 'djonga', 'emicida', 'dexter']

nome = str(input('Digite o nome de um artista ou banda: ')).strip().lower()
if nome in artistas:
    print('{} faz parte de nossa produtora'.format(nome))
else:
    print('Não faz parte de nossa produtora'.format(nome))