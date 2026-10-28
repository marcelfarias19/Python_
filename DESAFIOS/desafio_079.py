# crie um programa onde o usuário digite vários valores numéricos e cadastre em uma lista.


numeros = list()
resp = 'N'
while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    
    resp = str(input('Deseja continuar: [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-='*20)
numeros.sort()
print(f'Você digitou os valores {numeros}')
    
    