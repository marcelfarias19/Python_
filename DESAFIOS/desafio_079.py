# crie um programa onde o usuário digite vários valores numéricos e cadastre em uma lista.

num1 = []
num2 = num1
resp = 'N'
while True:
    num1.append(int(input('Digite um valor: ')))
    if num1 == num2:
        print('valor Duplicado não vai adicionar...')
    else:
        print('Valor adicionado com sucesso...')    
    
    resp = str(input('Deseja continuar: [S/N]')).strip().upper()
    if resp == 'N':
        break

print(f'Você digitou os valores {num2}')
    
    