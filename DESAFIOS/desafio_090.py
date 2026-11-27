# faça um programa que leia um nome e média de um aluno guardando tambem a situação em um dicionário. no final mostre o contéudo da estrutura na tela.

dados = {}
aluno = []
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input('média: '))
aluno.append(dados.copy())                # nesse exercício eu poderia ter usado o dados direto em vez de criar uma lista.

for c in aluno:
    for a, b in c.items():
        print(f'{a} é igual a {b}')
        
if dados['média'] >= 7 :
    print('Situação é igual a Aprovado') 
elif dados['média'] <= 6.99 and dados['média'] > 5:
    print('Situação do aluno é igual a Recuperação') 
else:
    print('Situação do aluno é igual a Reprovado')           

    
    