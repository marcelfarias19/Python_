# organizador de velocidades.

# Crie um programa que leia 5 valores numéricos representando para velocidade (frequências em Hz) e os insira em uma lista, mantendo os valores em ordem crescente desde o início.
# 1 - Crie uma lista vazia chamada velocidade.
# 2 - Use for com range(0, 5) para solicitar os 5 valores.
# 3 - Se a lista estiver vazia ou o valor for maior que o último elemento, adicione-o ao final com append(). 
# 4 - Caso contrário, percorra a lista usando while para encontrar a posição correta e insira o valor com insert().
# 5 - Mostre uma mensagem indicando se o valor foi adicionado ao final ou em outra posição.
# 6 - Ao terminar, mostre todos os valores em ordem crescente.

velocidade = []
for cont in range(0, 5):
    n = int(input('Digite a velocidade: '))
    if cont == 0:
        velocidade.append(n)
        print('Adcionado no final da lista')
    elif n > velocidade[-1]:
        velocidade.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos <= len(velocidade):
            if n < velocidade[pos]:
                velocidade.insert(pos, n)
                print(f'a posição da velocidade foi {pos}')
                break
            pos += 1
print('-='*20)
print(f'Os valores de velocidade adicionados foram {velocidade}')