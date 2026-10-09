# exercicio para treinar o in: ver se o valor esta dentro de uma coleção de dados.

jogos = ['zelda', 'god of war', 'gta', 'minicraft']

game = str(input('Digite o nome do jogo: ')).strip().lower()

if game in jogos:
    print('{} faz parte de nossa coleção'.format(game))
else:
    print('{} não faz parte de mnossa seleção'.format(game))