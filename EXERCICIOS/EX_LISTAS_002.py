# Exercícios de listas

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

'''for v in valores:
    print(f'{v}...', end=' ')'''
    
for c, v in enumerate(valores):    # O enumarate ele pega tanto a chave quanto o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista!')