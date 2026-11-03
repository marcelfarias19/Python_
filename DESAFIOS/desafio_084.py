# Faça um programa que leia várias pessoas guardando tudo em uma lista, no final mostre.
# A - Quantas pessoas foram cadastradas.
# B - Uma listagem com pessoas mais pesadas.
# C - Uma listagem com as pessoa mais leves.

lista = []
dados = []
quantidade = 0
maior = 0
menor = 0
resp = 'N'
while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))   
      
    quantidade += 1    
    
    if len(lista) == 0:            # é importante o len aqui para dara  referência para o menor número.
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]  
        if dados[1] < menor:
            menor = dados[1]
            
    lista.append(dados[:])       # Lista.append(dados[:]) serve para fazer uma cópia
    dados.clear()                # .clear() apaga o que foi adicionado a lista dados
            
    resp = str(input('Deseja continuar: [S/N]')).upper().strip() 
    if resp == 'N':
        break
           
print('-='*20)
print(f'você cadastrou {quantidade} pessoas')
print(f'O maior peso foi {maior:.2f} de ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'da pessoa {p[0]}')
print()
print(f'O menor peso foi {menor:.2f} de ', end=' ')
for p in lista:
    if p[1] == menor:
        print(f'da pessoa {p[0]}', end=' ')
print()
    