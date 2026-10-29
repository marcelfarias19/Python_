# Crie um organizador de preços.
# crie um programa que leia 5 preços de produtos e insira cada preço na posição correta, mantendo a ordem crescente durante a inserção.
# 1 - Crie uma lista chamada precos.
# 2 - Use for com range(0,5) para pedir os 5 preços.
# 3 - Se a lista estiver vazia ou o preço for maior que o ultimo elemento, adicione-o ao final com .append
# 4 - Caso contrário, percorra a lista com while e encontre a posição correta para inserir o preço usando .insert().
# 5 - Mostre uma mensagem indicando onde o preço foi adicionado.
# 6 - Ao terminar, mostre todos os preços em ordem crescente.
preco = []
for cont in range(0, 5):
    n = int(input('Digite um preço: '))    
    if cont == 0 or n > preco[-1]:
        preco.append(n)  
        print('Adiconado ao final da lista...')             
    else:
        pos = 0
        while pos < len(preco):
            if n <= preco[pos]:
                preco.insert(pos, n) 
                print(f'Adionado a posição {pos}') 
                break             
            pos += 1   
print('-='*20)    
print(f'Os preços em ordem foram {preco}')   
        