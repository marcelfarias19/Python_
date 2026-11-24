# Exercício prático.

'''def soma(a, b):
    print(f'A={a} e B={b}')
    s = a + b
    print(f'A soma A + B = {s}')

# programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)'''

# desempacotamento

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

# Programa principal
soma(5, 2)
soma(2, 9, 4)
