# criar um programa que lê vários números.
soma = 0
cont = 0
while True:
    n = int(input('Digite um valor: '))
    soma += n
    cont = cont + 1
    
    resp = str(input('Deseja continuar [S/N]')).upper().strip()
    if resp == 'N':
        break

print()
print(f'Foram digitados {cont} números e o total da soma é {soma}')