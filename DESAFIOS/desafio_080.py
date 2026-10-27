# Crie um programa onde o usuário possa digitar 5 valores e cadastre-os em uma lista, já na posição correta de inserção. (no final mostre a lista na tela q sem usar o sort)
num = []
valor = 0
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if not num:
        num.append(valor)
        
    elif valor < num[0]:
        num.insert(0, valor)        
    
    else:
        for v in num:
            if valor < v:
                posicao = num.index(v)
                num.insert(posicao, valor)
                break      
    
print(f'Os valores digitados foram {num}.')
    
    