#  Crie um programa onde os usúarios possa digitar 7 valores numéricos e os cadastre em uma lista única que mantenha separado os valores pares e ímpares, no final mostre os valores pares e ímpares em ordem crescente.
valor = []
lista = []

for c in range(0, 7):
    valor.append(int(input(f'digite o {c}° valor: ')))  
    
    lista.append(valor[:])
    valor.clear()  
    
print('-='*20)
print(f'Os números pares: ', end=' ')  
for p in lista:
    if p[0] % 2 == 0:
        print(f'[{p[0]}]', end=' ') 
print() 
print(f'os números ímpares: ', end=' ')
for p in lista:
    if p[0] % 2 == 1:
        print(f'[{p[0]}]', end=' ')
print()


    