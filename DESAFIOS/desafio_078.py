# Faça um programa que leia 5 valores numéricos e guarde em uma lista

num = []
for cont in range(0, 5):
    num.append(int(input(f'digite um valor na posição {cont}: ')))
    
print('-='*15)
print(f'Você digitou os valores {num}')
print(f'O maior numero é {max(num)}')
print(f'O menor número é {min(num)}')
        

