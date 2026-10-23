# Reforço do exercício

from random import randint
numeros = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)) 
# apredemos aqui que se pode colocar mais de 1 randint em uma tupla com (randint(1, 10))

print(f'os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\n O maior valor sorteado foi {max(numeros)}')  # aqui o \n para quebrar a linha.
print(f' O menor valor sorteado foi {min(numeros)}')

# Nesse exercício se busca o maior número com um método / max() para o maior valor - e min() para o menor valor.
    