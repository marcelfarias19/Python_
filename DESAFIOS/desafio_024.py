#programa que le o nome de uma cidade e vê se ela começa com "santo"

city = str(input('Digite o nome da cidade: ')).strip()
print(city[:5].upper() == 'SANTO')