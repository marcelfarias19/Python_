#Somador de números pares
SomaPar = 0
contapar = 0
for cont in range(1, 6 + 1):
    num = int(input('Digite o {} valor: '.format(cont)))
    if num % 2 == 0:
        SomaPar += num
        contapar = contapar + 1
            
print('Você informou {} valores a soma dos números pares é {}'.format(contapar, SomaPar))