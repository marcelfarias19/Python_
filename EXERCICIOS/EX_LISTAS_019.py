# Crie um programa que cadastre vários funcionários, armazenando os dados da empresa em uma lista composta
# Para cada funcionário nome/idade/salário
# O programa deve continuar cadastrando enquanto o usuário desejar. no final mostre.
# Quantos funcionários foram cadastrados 
# Uma listagem com o nome de todos os funcionários que recebem o maior salário.
# Uma listagem com o nome de todos os funcionários que recebem o menor salário. 
# A média salarial dos funcionãrios.

lista = []
dados = []
resp = 'N'
maior = 0
menor = 0
quantidade_funcionario = 0
somatoria_salario = 0
media_salario = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('idade: ')))
    dados.append(float(input('Salário: '))) 
    
    if len(lista) == 0:
        maior = menor = dados[2]
    else:
        if dados[2] > maior:
            maior = dados[2]
        if dados[2] < menor:
            menor = dados[2]
            
    quantidade_funcionario += 1         
    somatoria_salario += dados[2]
    media_salario = somatoria_salario / quantidade_funcionario        
    lista.append(dados[:])  
    dados.clear()   
    
    resp = str(input('Deseja continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break

print('-='*20)
print(f'Você cadastrou {quantidade_funcionario} pessoas')
print(f'os funcionários que recebem o maior salário {maior:.2f} ', end=' ')
for p in lista:
    if p[2] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'Os funcionários que recebem o menor salário {menor:.2f} ', end=' ')
for p in lista:
    if p[2] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print(f'A média salárial é de R$ {media_salario:.2f}')

    



     
        