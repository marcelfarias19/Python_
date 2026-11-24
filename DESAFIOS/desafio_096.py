# faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular       ( largura e comprimento) e mostre a área do terreno.

def area(a, b):
    s = a * b
    print(f'A área de um terreno {a} x {b} é de {s} M² ')
    
def titulo(txt):
    print('-='*15)
    print('>> CONTROLE DE TERRENOS <<')
    print('-='*15)
    
# programa principal
titulo('')
a = float(input('LARGURA (M): '))
b = float(input('COMPRIMENTO (M): '))
area(a, b)