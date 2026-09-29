#programa que le o nome de uma cidade e vê se ela começa com "santo"

city = input('Digite o nome da cidade: ')
print('essa cidade tem a palavra santo: {}'.format(city.startswith('Santo')))