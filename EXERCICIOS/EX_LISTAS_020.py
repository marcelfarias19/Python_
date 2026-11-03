# Cadastro de veiculos.
# para cada veiculo, solicite: modelo do veículo, Ano de fabricação, preço.
# o programa deve continuar cadastrando enquanto o usuário desejar.
# No final mostre.
# Quantos veículos foram cadastrados.
# Uma listagem com modelos dos veículos mais caros.
# Uma listagem com modelos dos veículos mais baratos.
# A soma dos preços de todos os veículos.
# A média dos preços dos veículos cadastrados.

dados = []
lista = []
mai_carro = 0
men_carro = 0
resp = 'N'
soma_car = 0
media_car = 0
quantidade = 0
while True:
    dados.append(str(input('Modelo do carro: ')))
    dados.append(int(input('Ano de fabricação: ')))
    dados.append(float(input('Preço: ')))
    
    if len(lista) == 0:
        mai_carro = men_carro = dados[2]
    else:
        if dados[2] > mai_carro:
            mai_carro = dados[2]        
        if dados[2] < men_carro:
            men_carro = dados[2]
    
    quantidade += 1
    soma_car += dados[2]
    media_car = soma_car / quantidade
    lista.append(dados[:])
    dados.clear()
    
    resp = str(input('Deseja continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break

print('-='*20)
print(f'A quantidade de veículos cadastrados foram: {quantidade}')
print(f'Os veículos mais caros tem o valor {mai_carro:.2f} e são', end=' ')
for p in lista:
    if p[2] == mai_carro:
        print(f'[{p[0]}]', end=' ')
print()
print(f'Os veículos mais baratos tem o valor de {men_carro:.2f} e são', end=' ')
for p in lista:
    if p[2] == men_carro:
        print(f'[{p[0]}]', end=' ')
print()
print(f'A soma dos veículos é de {soma_car}')
print(f'A média dos valores dos veículos é de {media_car:.2f}')
    

            
    