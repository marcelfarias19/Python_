#comparador de valores
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('digite o segundo valor: '))

if num1 > num2:
    print('{} é maior que {}.'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}.'.format(num2, num1))
else:
    print('{} e {} são números iguais.'.format(num1, num2))