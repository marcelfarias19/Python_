# reforço do exercício 078.

num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input(f'digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
               
print('-='*15)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} na posição ', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} na posição', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end=' ')
print()
