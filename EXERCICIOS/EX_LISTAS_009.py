# Cadastro de jogos
# Crie um programa em python que cadastre códigos de jogos em uma lista.
# 1 - Peça ao usuário para digitar um código numérico de jogo.
# 2 - Se o código ainda não estiver na lista, adicione-o e mostre uma mensagem de sucesso.
# 3 - Se o código já estiver cadastrado, avise que ele é duplicado e não o adicione.
# 4 - Pergunte se deseja continuar: [S/N]
# 5 - Se responder 'N', encerre o programa usando break
# 6 - Ao final, organize os códigos em ordem crescente e mostre na lista.

jogos = list()
resp = 'N'
while True:
    n = int(input('Digite o código do jogo: '))
    if n not in jogos:
        jogos.append(n)
        print('Código adicionado com sucesso.')
    else:
        print('Código duplicado! Não vpou adicionar.')
    
    resp = str(input('Você deseja continuar: [S/N]')).upper().strip()
    if resp == 'N':
        break
print('-='*20)
jogos.sort()
print(f'Os códigos cadastrados foram {jogos}')