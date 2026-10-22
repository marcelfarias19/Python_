# exercícios de tuplas. (reforço)

extenso = ('cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

num = int(input('Digite um número entre 5 e 10: '))

while True:
    
    if num < 5 or num > 10:
        num = int(input('ERROR: tente novamente, digite um valor entre 5 e 10: '))
    else:
        print(f'Você digitou o número {extenso[num - 5]}')
        break