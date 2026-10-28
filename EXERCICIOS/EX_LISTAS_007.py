# crie um programa que permita cadastrar códigos númericos de produtos.
# 1 - Pedir ao usuário que cadastre um número inteiro.
# 2 - Verificar se o código já esta na lista.
# 3 - Se não estiver, adicionar o código.
# 4 - se já estiver, Avisar que o código é duplicado
# 5 - Perguntar se o usuário deseja continuar o cadastro.
# 6 - Quando terminar, mostrar todos os códigos cadastrados em ordem crescente.

codigo = list()
resp = 'N'
while True:
    n = int(input('Digite o código do produto: '))
   
    if n not in codigo:
        codigo.append(n)
        print('código adicionado com sucesso.')
    else:
        print('código duplicado! Não vou adicionar.')
    
    resp = str(input('Você deseja continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-='*20)
codigo.sort()
print(f'Os códigos cadastrados foram {codigo}')
    
    
    