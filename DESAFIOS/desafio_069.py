# criar um programa que leia várias vezes o nome e o sexo das pessoas.

pessoas_18_mais = 0
homem_cadastro = 0
mulheres_20 = 0

while True:
    print('=-'*15)
    print('-- CADASTRO DE PESSOAS --'.center(40))
    print('=-'*15)
    
    idade = int(input('idade: '))
    sexo = str(input('sexo: [M/F] ')).upper().strip()
            
    if  idade >= 18:
        pessoas_18_mais += 1       
  
    if sexo == 'M':
        homem_cadastro += 1 
        
    if sexo == 'F' and idade >= 20:
        mulheres_20 += 1    
    
    print('='*15)
    resp = str(input('Deseja continuar: [S/N]')).upper().strip()
    if resp == 'N':
        break

print()
print(f'Quantas pessoas tem mais de 18 anos: {pessoas_18_mais} ')
print(f'Quantos homens foram cadastrados: {homem_cadastro} ')
print(f'Quantas mulheres tem mais de 20 anos: {mulheres_20}')
