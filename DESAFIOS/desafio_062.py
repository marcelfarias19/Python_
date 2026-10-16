#melhorando o desafio 061
print()
print('--Progressão aritmética--')
print()  

c1 = int(input('Digite o valor do primeiro termo aritmético: '))
c2 = int(input('Digite o valor da razão aritmética: '))
print()

c3 = 0
cont = 1
    
while cont <= 10 :    
    
    print(c1)
    c3 = c1 + c2
    c1 = c3       
    cont = cont + 1
    print(c3)   
    
print()

n = int(input('deseja mostrar mais quantos termos? (lembrando que 0 encerra!): '))    

while n != 0:
    cont = 1
    
    while cont <= n:
        print(c1)
        c1 = c1 + c2
        cont = cont + 1

    n = int(input('Deseja mostrar mais quantos termos? (0 para encerrar): '))
    
print()
print('Fim da execução!')