#programa que lê nome,idade,sexo de 4 pessoas.
#mostre média de idade / Qual o nome do homem mais velho / quantas mulheres tem menos de 20 anos.

print('-----------------------')
print('--LEITOR DE PESSOAS--')
print('-----------------------')

mediaidade = 0
somaidade = 0
homem_mais_velho = 0
homem_mais_idade = 0
mulhermaior = 0

for cont in range(1, 4+1):
    nome = str(input('{}° Digite seu nome: '.format(cont)))
    idade = int(input('{}° Digite sua idade: '.format(cont)))
    sexo = str(input('{}° Digite seu sexo [M / F]: '.format(cont))).upper()
    print('--------------------------------------')
    
    somaidade += idade
    mediaidade = somaidade / 4
    
    if idade > homem_mais_idade:
        homem_mais_idade = idade
        homem_mais_velho = nome
        
    if sexo == 'F' and idade > 20:
        mulhermaior += 1   
    
print('A média da idade das pessoas é de {}'.format(mediaidade))
print('Qual o nome do homem mais velho: {}'.format(homem_mais_velho))
print('Quantas mulheres tem mais de 20 anos: {}'.format(mulhermaior))
    