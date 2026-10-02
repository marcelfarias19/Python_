#programa para ler as dimensões e falar qual triângulo é.

val1 = float(input('Digite a primeira distância: '))
val2 = float(input('Digite a segunda distância: '))
val3 = float(input('Digite a terceira distância: '))

if val1 == val2 and val2 == val3 :
    print('Esses Valores formam um triângulo equilátero.')
elif val1 == val2 or val1 == val3 or val2 == val3 :
    print('Esse é um triângulo isósceles.')
elif val1 != val2 and val1 != val3 and val2 != val3:
    print('Esse é um triângulo escaleno. ')   