#Somador de números pares
SomaPar = 0
for cont in range(1, 6 + 1):
    num = int(input('Digite o {} valor: '.format(cont)))
    if num % 2 == 0:
        SomaPar += num
            
print('O valor da soma dos números pares é {}'.format(SomaPar))