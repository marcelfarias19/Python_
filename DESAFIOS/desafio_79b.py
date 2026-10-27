# reforço do desafio 079

num1 = []
num2 = num1
maior = 0
menor = 0
resp = 'N'
cont = 0
while True:
    num1.append(int(input('Digite um valor: ')))
    if num1 == num2:
        print('valor Duplicado não vai adicionar...')
    else:
        print('Valor adicionado com sucesso...')  
       
    if num2[cont] > maior:
        maior = num2[cont]
        
    if cont == 0:
        menor = num2[cont]
    elif num2[cont] < menor:
        menor = num2[cont]
    
    resp = str(input('Deseja continuar: [S/N]')).strip().upper()
    if resp == 'N':
        break

print(f'Você digitou os valores {num2}')
print(f'O maior valor digitado foi {maior} na posição')
print(f'O menor valor digitado foi {menor} na posição')