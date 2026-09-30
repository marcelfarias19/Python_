#programa de leitura de numeros.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('{} é o maior número.'.format(num1))
elif num2 > num1 and num2 > num3:
    print('{} é o maior número.'.format(num2))
else:
    print('{} é o maior número.'.format(num3))
    
if num1 < num2 and num1 < num3:
    print('{} é o menor número.'.format(num1))
elif num2 < num1 and num2 < num3:
    print('{} é o menor número.'.format(num2))
else:
    print('{} é o menor número.'.format(num3))


    

