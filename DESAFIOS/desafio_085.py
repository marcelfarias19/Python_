# Crie um programa que vai ler vários números e colocar em ujma lista. depois disso crie duas listas extras que vão conter apenas valores pares e os valores impares digitados respectivamente.
# Ao final mostre o conteúdo das 3 listas.

lista = []
par = []
impar = []
resp = 'N'
while True:
    n = int(input('Digite o valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
    else:
       lista.append(n)
    resp = str(input('Você deseja continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
        
