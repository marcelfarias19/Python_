# exercícios do laço while com break

'''cont = 1
while cont <= 10:
    print(cont, '->', end=' ')
    cont += 1
print('acabou')'''

soma = 0
n = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')