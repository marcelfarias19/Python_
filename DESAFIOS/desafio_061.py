#exercício que lê uma PA (progressão aritmética)

c1 = int(input('Digite o valor do primeiro termo aritmético: '))
c2 = int(input('Digite o valor da razão aritmética: '))

print(c1)
c3 = 0
cont = 1
while cont <= 10:
    c3 = c1 + c2
    c1 = c3
    
    cont = cont + 1
    print(c3)