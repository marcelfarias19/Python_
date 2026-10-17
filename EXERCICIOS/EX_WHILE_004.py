#exercício que lê uma PA (progressão aritmética)

c1 = int(input('Digite o valor do primeiro termo aritmético: '))
c2 = int(input('Digite o valor da razão aritmética: '))

c3 = c1
cont = 1
tot = 0
mais = 10
while mais != 0: 
    tot = tot + mais  
    while cont <= tot  :
        print('{} '.format(c3), end=' ')
        c3 = c3 + c1            
        cont = cont + 1
       
    print('PAUSA')
    mais = int(input('Quantos termos adicionais você gosgtaria de mostrar? '))

print('Fim da execução')