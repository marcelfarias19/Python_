#programa para descobrir se uma frase é um palindromo
print('-- Programa para achar um palindromo --')
fra = str(input('Digite uma frase:')).strip().upper()
palavra = fra.split()
junto = ''.join(palavra)
#inverso = ''
inverso = junto[::-1] 


#for letra in range(len(junto) - 1, -1, -1):
    #inverso += junto[letra] 
        
print('O inverso de {} é {}'.format(junto, inverso))
    
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')

