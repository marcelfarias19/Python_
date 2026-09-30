#programa para aumento de salário

sal = float(input('digite o valor do seu salário: '))

if sal >= 1250.00:
    aumento = sal * 1.1
    print('Seu novo salário é R$ {:.2f}.'.format(aumento))
else:
    sal < 1250.00
    aumento = sal * 1.15
    print('Seu novo salário é R$ {:.2f}.'.format(aumento))