# Cadastro de produtos de estoque.
# Crie um programa que cadastre vários produtos de uma loja.                                              para cada um solicite:
# Nome do produto/ quantidade / preço unitário
# O programa deve continuar cadastrando enquanto o usuário desejar.Ao finalizar cadastro mostre:
# Uma listagem com todos os produtos
# quantidade em estoque
# O valor total de estoque (quantidade x preço de cada produto)
# produto mais caro
# A média dos preços dos produtos.
# Consulta de produtos - pergunte qual produto o usuário deseja consultar
# utilize o número de indentificação (índice) apresentandoa  listagem
# Mostre o nome, a quantidade e o preço do produto escolhido.
# digitar 999 para encerra consulta.

print('-='*45)
print(' >> CADASTRO DE PRODUTOS << '.center(90))
print('-='*45)

dados = []
lista = list()
resp = 'N'

while True:
    dados.append(str(input('Nome do produto: ')))
    dados.append(int(input('Quantidade: ')))
    dados.append(float(input('Preço: ')))
    lista.append(dados[:])
    dados.clear()
    
    resp = str(input('Deseja continuar: [S/N]: ')).upper().strip()
    if resp == 'N':
        break
    
print('-'*100)
valor_total = 0
mais_caro = 0
media = 0
somador = 0
print('N° NOME PRODUTO:           QUANTIDADE/ESTOQUE:          PREÇO UNITÁRIO:         VALOR TOTAL:')
for i, c in enumerate(lista):
    valor_total = c[1] * c[2]
    somador += c[2] 
    media = somador / len(c)
    print(f'{i}  {c[0]: <30} {c[1]: <26}R${c[2]: <20} R${valor_total}')
    if c[2] > mais_caro:
        mais_caro = c[2]
print('-'*100)
print(f'A média dos valores é {media:.2f}')
print(f'O produto mais caro é {mais_caro} /', end=' ')
for i, c in enumerate(lista):
    if mais_caro == c[2]:
        print(f'{c[0]}', end=' ')
print()
print('-'*100)
cont = 0
while cont != 999:
    cont = int(input('Qual produto o usuário deseja consultar: (999 interrompe a busca) '))  
    for i, c in enumerate(lista):
        if cont == i:
            print('N° NOME PRODUTO:           QUANTIDADE/ESTOQUE:          PREÇO UNITÁRIO:         VALOR TOTAL:')
            print(f'{i: <4}  {c[0]: <28} {c[1]: <24} R${c[2]: <19} R${c[1]*c[2]:.2f}') 
            print('-'*100)     
print('='*100)
print('FINALIZADO')
print('>> VOLTE SEMPRE <<')
