#programa que lê vários números e para no 999.
print()
print('--Contador e Somador--')
print('O programa para quando o usúario digitar 999.')
print()


num_digitados = 0
soma_num = 0
while True:       # importante aprender usar todos os operadores lógicos
 
    num = int(input('Digite números inteiros: ')) 
    if num == 999:
        break         # O break aqui quebra o laço mas nao computa o ultimo num inteiro a soma
        
    num_digitados = num_digitados + 1  
    soma_num += num  
   
    
print()
print('{} números foram digitados'.format(num_digitados))
print('A soma de {} números digitados é {}'.format(num_digitados, soma_num))
print()
print('Fim da execução')