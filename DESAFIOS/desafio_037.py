#conversão para binário,octal,hexadecimal
num = int(input('Digite um número: '))
print('''Escolha uma das bases da conversão.
[1] para Binário 
[2] para Octal 
[3] para hexadecimál''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÀRIO é igual a {}.'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)))
else:
    print('Opção inválida.')

