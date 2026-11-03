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
quantidade_funcionario = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('idade: ')))
    dados.append(float(input('Salário: ')))
    
    quantidade_funcionario += 1
    
    