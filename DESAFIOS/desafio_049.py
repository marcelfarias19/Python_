#refazendo a  tabuada do exercício 009

tab = int(input('Digite o número que deseja a tabuada: '))

for cont in range (1, 10 + 1 ):
    result = tab * cont
    print('{} x {} = {}'.format(tab, cont, result ))
    