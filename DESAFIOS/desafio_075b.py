# reforço do exercício 075.
print()
num = (int(input('Digite um número: ')),   # aqui Você pode fazer uma tupla pedir 4 valores através desse 
       int(input('Digite outro número: ')),   # método, 
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valortes {num}')
print()
print(f'O valor 9 apareceu {num.count(9)} vezes')
# aqui o método .count() serve para contar quantas vezes aparece o número na tupla

if 3 in num:   # if é usado para procurar o 3 dentro da tupla e se não é achado ele retorna que nao achou
    print(f'O valor 3 apareceu na posição {num.index(3)+1} Posição') # index é usado para achar a posição
else:
    print('O valor 3 não foi digitado em nenhuma posição')
    
print('Os valores pares digitados foram ', end=' ') # o end=' ' aqui serve para manter o resultado do for na mesma linha
for n in num:        # aqui é usado um for com uma variavel n para guardar o números pares 
    if n % 2 == 0:
        print(n, end=' ') # esse end=' ' aqui tbm serve para manter o resultado na mesma linha2396
    

