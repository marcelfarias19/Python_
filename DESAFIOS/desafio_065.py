#crie um programa que leia vários números no final da execução mostrar a média deles
print()
print('--LEITURA DE NÚMEROS--')
print()

somador_num = 0
media_valor = 0
maior_valor = 0
menor_valor = 0
cont = 1
while True:
    
    num = int(input('digite um valor: '))     
        
    if cont == 1:    
        menor_valor = num
    elif num < menor_valor:
        menor_valor = num 
        
    if cont == 1:
        maior_valor = num    
    elif num > maior_valor:
            maior_valor = num
        
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()        
    if resp == 'N':
        break
    
    somador_num += num
    media_valor = somador_num / cont
    cont = cont + 1 

print()
print('A média dos valores é {:.2f}'.format(media_valor))
print('O maior Valor é {}'.format(maior_valor))
print('O menor valor é {}'.format(menor_valor))
print()
print('Fim da execução do programa')
