# Crie um programa onde o usuário possa digitar 5 valores e cadastre-os em uma lista, já na posição correta de inserção. (no final mostre a lista na tela q sem usar o sort)
    
lista = []
for cont in range(0, 5):
    n = int(input('Digite um valor: ')) 
    if cont == 0:
        lista.append(n)
        print('Adicionado no final da lista')
    elif n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n < lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-='*20)
print(f'Os valores adiconados foram {lista}')
            
        