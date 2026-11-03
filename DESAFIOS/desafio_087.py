# Aprimore o desafio anterior, mostrando.
# A soma de todos os valores pares digitadosa.
# A soma de todos os valores somados da terceira coluna.
# O maior valor da terceira linha.

matriz = []
par = 0
soma_coluna_3 = 0
maior = 0
for l in range(0, 3):
    lista = []
    for c in range(0, 3):
        lista.append(int(input(f'Digite um valor para {l, c}: ')))
    matriz.append(lista)
    
print('-='*20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l] [c]}]', end=' ')
    print()

print()

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
               
print(f'A soma dos valores pares: {par} ')

for l in range(0, 3):
    soma_coluna_3 += matriz[l][2]

print(f'A soma dos valores da terceira coluna: {soma_coluna_3}')

for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior valor da segunda linha: {maior}')