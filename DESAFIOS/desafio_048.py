#Somadores de números primos

soma = 0
contador = 0 
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma = soma + cont
        contador = contador + 1
         
print('A soma de todos os valores {} solicitados é {}'.format(contador, soma))