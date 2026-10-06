#progressão aritmética

c1 = int(input('Digite o valor do primeiro termo aritmético: '))
c2 = int(input('Digite o valor da razão aritmética: '))
c3 = 0

print(c1)
for i in range(1, 10 + 1):
    c3 = c1 + c2 
    c1 = c3
    print(c3)