# Programa com tupla totalmente preenchida com uma contagem por extenso de zero a vinte.

extenso = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'onze', 'doze', 'treze', 'Quartoze', 'Quinze', 'Dezesseis', 'dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))

while True:
    
    if num < 0 or num > 20:
        num = int(input('Tente novamente. digite um número entre 0 e 20: '))
    else:
        print(f'você digitou o número {extenso[num]}')
        break

    
   