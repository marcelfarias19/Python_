# Crie um programa que vai ler vários números e colocar em uma lista e depois disso mostre.
# Quantos números foram digitados.
# A lista de valores em ordem decrescente.
# e Se o valor 5 for digitado e está na lista.

lista = []
resp = 'N'
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('Você deseja continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('-='*20)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
    

