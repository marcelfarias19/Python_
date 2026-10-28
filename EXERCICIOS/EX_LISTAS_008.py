# cadastros de números de telefones:
# Crie um programa em python que resgistre números de telefone em uma lista, seguindo estas regras.
# 1 - peça o ujsuário para digitar um número de telefone.
# 2 - Se o número ainda não estibver na lista, Adicione-o é mostre uma mensagem de sucesso.
# 3 - Seo número já estiver cadastrado, mostre ujma mensagem avisando que ele é duplicado e não o adicione novamente.
# 4 - Pergunte se o usuário deseja continuar: [S/N]
# 5 - Se responder N encerre o programa usando break.
# 6 - Ao finalizar, mostre todos os números cadastrados em ordem crescente.

telefone = list()
resp = 'N'
while True:
    n = int(input('Digite um número de telefone: '))
    
    if n not in telefone:
        telefone.append(n)
        print('Número cadastrado com sucesso')
    else:
        print('Número duplicado! Não vou adicionar')
        
    resp = str(input('você deseja continuar: [S/N]')).upper().strip()
    if resp == 'N':
        break
print('-='*20)
telefone.sort()
print(f'Os números cadastrados foram {telefone}')
        