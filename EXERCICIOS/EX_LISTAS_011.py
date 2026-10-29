# Organizador de notas musicais
# Crie uma lista que leia 5 valores numéricos representando notas musicais (frequência em hz) e os insira  em uma lista, mantendo os valores em ordem crescente desde o início.
# 1 - Crie uma lista vazia chamada frequências.
# 2 - Use for range(0, 5) para solicitar os 5 valores.
# 3 - Se a lista estiver vazia ou o valor for maior que o último elemento.
# 4 - Caso contrário, percorra  a lista usando while para encontrar a posição correta  e insira o valor com insert.
# 5 - Mostre uma mensagem indicando se o valor for adicionado ao final oua  outra posição.
# 6 - Ao termianr, mostre todos os valores em ordem crescente.

frequencia = []
for cont in range(0,5):
    n = int(input('Digite uma frequência: '))
    if cont == 0:
        frequencia.append(n)
        print('Adicionado ao final da lista')
    elif n > frequencia[-1]:
        frequencia.append(n)
        print('Adicioando ao final da lista')
    else:
        pos = 0
        while pos < len(frequencia):
            if n < frequencia[pos]:
                frequencia.insert(pos, n)
                print(f'Adicionado a posição {pos}')
                break
            pos += 1  
print('-='*20)
print(f'Os valores em ordem foram {frequencia}')
            
    
     