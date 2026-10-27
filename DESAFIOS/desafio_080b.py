#reforço do exercício 080 (digitar 5 valores e falar as posições)
lista = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > lista[-1] :      # se for igual a o primeiro valor ele adiciona o valor na posição 0
        lista.append(n)
        print('Adicionado ao final da lista da lista')    
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')   
                break
            pos += 1
print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')
        