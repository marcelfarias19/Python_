# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços.

produtos = (
    'Smartphone', 2500,
    'Notebook', 4200,
    'Teclado', 150,
    'Mouse', 80,
    'Monitor', 1100,
    'Headseat', 250,
    'Webcam', 180,
    'Impressora', 750,
    'Tablet', 1600,
    'Smartwatch', 400
)

print('-='*30)
print('LISTAGEM DE PRODUTOS'.center(60))
print('-='*30)
print(f'{produtos[0]:.<40} R$ {produtos[1]}')
print(f'{produtos[2]:.<40} R$ {produtos[3]}')
print(f'{produtos[4]:.<40} R$ {produtos[5]}')
print(f'{produtos[6]:.<40} R$ {produtos[7]}')
print(f'{produtos[8]:.<40} R$ {produtos[9]}')
print(f'{produtos[10]:.<40} R$ {produtos[11]}')
print(f'{produtos[12]:.<40} R$ {produtos[13]}')
print(f'{produtos[14]:.<40} R$ {produtos[15]}')
print(f'{produtos[16]:.<40} R$ {produtos[17]}')
print(f'{produtos[18]:.<40} R$ {produtos[19]}')

# Aprendemos a usar (:.<30) na tupla para fazer o ajuste na lista com os pontos