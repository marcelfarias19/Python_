#programa que fale os valores são um triangulo.

val1 = float(input('Digite a primeira distância: '))
val2 = float(input('Digite a segunda distância: '))
val3 = float(input('Digite a terceira distância: '))

if val1 + val2 > val3 and val1 + val3 > val2 and val2 + val3 > val1:
    print('Esses Valores forma um triângulo.')
else:
    print('esses valores não formam um triângulo.')  
    

