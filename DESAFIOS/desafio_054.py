#programa para ler o ano de nascimento de 7 
# e mostrar quantas atingiram a maior idade.

print('-----------------------------')
print('-- Contador de Idade --')
print('-----------------------------')

menoridade = 0 
maioridade = 0

for cont in range(1, 7+1):
    ano = int(input('{}° Digite o ano do seu nascimento: '.format(cont)))
    idade = 2026 - ano
    if idade < 18:
        menoridade += 1
    elif idade > 18:
        maioridade += 1       
                   
print('-----------------------------------')
print('{} pessoas são menores de idade'.format(menoridade))
print('{} pessoas são maiores de idade '.format(maioridade))
         
    
    