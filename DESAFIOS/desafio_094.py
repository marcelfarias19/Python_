# Crie um programa que leia nome, sexo e idade de várias pessoas guardando os dados de várias pessoas em um dicionário e todos os dicionários em uma lista,  no final mostre:
# - Quantas pessoas foram cadastradas.
# - A média da idade do grupo.
# - Uma lista com todas as mulheres.
# - uma lista com a idade a cima da média. 

resp = 'N'
pessoas = {}
lista = []
p_cadastro = 0
soma_idade = 0
media_idade = 0
m_cadastro = []
acima_media = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = int(input('idade: '))
    pessoas['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
    lista.append(pessoas.copy())
    
    p_cadastro += 1
    soma_idade += pessoas['idade']
    media_idade = soma_idade / p_cadastro    
    
    for v in pessoas.values():
        if v == 'F':
            m_cadastro.append(pessoas['nome'])                    
                        
    resp = str(input('Você deseja continuar: [S/N]')).upper().strip()
    if resp == 'N':
        break
    
print('-='*30)    
print(f'- O grupo tem {p_cadastro} pessoas.')
print(f'- A média da idade é de {media_idade:.2f}')         
print(f'- As mulheres cadastradas foram: ', end=' ')
for v in m_cadastro:
    print(f'{v}', end=' ')
print()
print('- Lista das pessoas que estão acima da média: ') 
for pessoa in lista:
    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa)  
for p in acima_media:
    for k, v in p.items():
            print(f'{k} = {v};', end=' ')            
    print()
print()
print('>> ENCERRADO <<')
    
