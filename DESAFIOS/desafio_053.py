#programa para descobrir se uma frase é um palindromo
print('-- Programa para achar um palindromo --')
fra = str(input('Digite uma frase:')).strip()
fra[::-1]
print('-----------------------------------')
print('Frase / palavra: {}'.format(fra))
print('Frase invertida / palavra: {}'.format(fra[::-1]))
print('-----------------------------------')

if fra == fra[::-1]:
    print('é um palíndromo')
else:
    print('Não é um palíndromo')
    
print('------------------------------------')

