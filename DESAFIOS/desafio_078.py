# Faça um programa que leia 5 valores numéricos e guarde em uma lista

num = []
for cont in range(0, 5):
    num.append(int(input('digite um valor: ')))
    
print('-='*15)
print(f'O maior numero é {max(num)}')
print(f'O menor número é {min(num)}')
        

