# organizador de velocidades.

# Crie um programa que leia 5 valores numéricos representando notas musicais (frequências em Hz) e os insira em uma lista, mantendo os valores em ordem crescente desde o início.
# 1 - Crie uma lista vazia chamada frequencias.
# 2 - Use for com range(0, 5) para solicitar os 5 valores.
# 3 - Se a lista estiver vazia ou o valor for maior que o último elemento, adicione-o ao final com append(). 
# 4 - Caso contrário, percorra a lista usando while para encontrar a posição correta e insira o valor com insert().
# 5 - Mostre uma mensagem indicando se o valor foi adicionado ao final ou em outra posição.
# 6 - Ao terminar, mostre todos os valores em ordem crescente.

velocidade = []
for cont in range(0, 5):
    n = int(input('Digite uma velocidade: '))
    if cont == 0:
        velocidade.append(n)
        print('Adicionado ao final da lista')
    if n > velocidade[-1]:
        velocidade.append(n)
        print('Adiconado ao final da lista')
    else:
        pos = 0
        while pos < len(velocidade):
            if n < velocidade[pos]:
                velocidade.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-='*20)
print(f'Os valores adicionados em ordem foram {velocidade}')