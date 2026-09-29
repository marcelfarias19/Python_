#fazer um programa que mostre as posições da letra 'a'

frase = str((input('digite uma frase: '))).upper()
print(frase.count('A'))
print(frase.find('A') + 1)
print(frase.rfind('A') + 1)