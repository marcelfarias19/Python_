# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

matriz = []
for l in range(0, 3):
    lista = [] 
    for c in range(0, 3):
        lista.append(int(input(f'digite um valor para {l, c}: ')))                
    matriz.append(lista)  
    
print('-='*20)      
        
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l] [c]}]', end=' ')
    print()