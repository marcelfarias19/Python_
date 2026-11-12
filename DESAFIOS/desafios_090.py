# faça um programa que leia um nome e média de um aluno guardando tambem a situação em um dicionário. no final mostre o contéudo da estrutura na tela.

dados = {}
aluno = []
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input('média: '))
aluno.append(dados.copy())

for c in aluno:
    for a, b in c.items():
        print(f'{a} é igual a {b}')
        
if dados['média'] >= 6 :
    print('Situação é igual a Aprovado') 
else:
    print('situação é igual a Reprovado')             

    
    