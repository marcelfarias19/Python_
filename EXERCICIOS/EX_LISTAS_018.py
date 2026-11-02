# exercício de matriz

matriz = list()

for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        valor = int(input(f'digite um valor para [{l}, {c}]'))
        linha.append(valor)            
    matriz.append(linha)    
    
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz [l][c]} ]', end=' ')
    print()