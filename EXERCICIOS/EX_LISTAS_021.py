# Analise de matriz
# A matriz de organizada em formato 3x3.
# A soma de todos os números ímpares.
# A soma dos valores da primeira coluna.
# O maior valor da terceira coluna.
# A média de todos os valores da matriz.
# quantos números são maiores que 5.

matriz = []
impar = 0
soma_coluna01 = 0
maior_coluna03 = 0
media_matriz = 0
somatorio = 0
quantidade_valores = 0
num_maior_05 = 0

for l in range(0, 3):
    lista = []
    for c in range(0, 3):
        lista.append(int(input(f'digite o valor {l, c}: ')))
    matriz.append(lista)
    
print(f'-='*20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
        
print('-='*20)

for l in range(0,3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 1:
            impar += matriz[l][c]
            
print(f'A soma dos valores ímpares: {impar}')

for l in range(0, 3):   
    soma_coluna01 += matriz[l][0]
        
print(f'A soma dos valores da primeira coluna: {soma_coluna01}')

for l in range(0, 3):
    if matriz[l][2] > maior_coluna03:
        maior_coluna03 = matriz[l][2]

print(f'O maior valor da coluna 3: {maior_coluna03}')

for l in range(0, 3):
    for c in range(0, 3):
        somatorio += matriz[l][c]
        quantidade_valores += 1
        media_matriz = somatorio / quantidade_valores
        
print(f'A média de todos os valores da matriz: {media_matriz:.2f}')

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] > 5:
            num_maior_05 += 1

print(f'Quantos números são maiores que 5: {num_maior_05}')