# Criar programa que lê o nome e o preço de vários produtos.

total_gastos = 0
produtos_mais = 0
produto_mais_barato = 0
mais_barato = 0
cont = 1
while True:
    print('=-'*15)
    print('-- CADASTRO DE PRODUTOS --'.center(30))
    print('=-'*15)
    
    produto = str(input('Digite o nome do produto: ')).upper().strip()
    preco = float(input('digite o valor do produto: '))   
   
    total_gastos += preco
        
    if preco >= 1000:
        produtos_mais += 1
        
    if cont == 1:
        mais_barato = preco
        produto_mais_barato = produto
    elif preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = produto   
    
    resp = str(input('Deseja continuar: [S/N]')).upper().strip()
    if resp == 'N':
        break

print('-='*20)
print('--FIM DO PROGRAMA!--'.center(40))
print('-='*20)
print(f'Qual é o total gasto nas compras: {total_gastos:.2f} R$')
print(f'Quantos produtos custam mais de 1000 reais: {produtos_mais}')
print(f'Qual é o nome do produto mais barato: {produto_mais_barato}')