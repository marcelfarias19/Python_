# reforço do exercício 076 

listagem = (
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
print('LISTAGEM DE PREÇOS'.center(60))
print('-='*30)

for pos in range(0, len(listagem)): # aqui é usando um range que começa na posição zero e vai ate o tamanho
    if pos % 2 == 0:                # de len() , aqui no caso no tamanho de listagem. 
        print(f'{listagem[pos]:.<30}', end=' ') # o end aqui deixa o else na mesma linha e o :.<30 alinhado 
    else:                                       # a direita deixa os pontos 
        print(f'R$ {listagem[pos]:>8.2f}')
        
# aqui if busca as posições pares para deixar de um lado da listagem 
# O else é imprimido do outro lado com :8 para regular a distância