#exercício que lê uma PA (progressão aritmética)

km1 = int(input('Quantos quilomêtros o atleta vai percorrer: '))
km2 = int(input('Quantos quilomêtros a distância aumentará a cada treino: '))
km3 = 0

mais = 5
tot = 0
cont = 1
while mais != 0: 
    tot = tot + mais  
    while cont <= tot:
        print('{} km'.format(km3), end=' ')
        km3 = km1 + km2
        km1 = km3    
        cont = cont + 1
    print('pausa')
    mais = int(input('Quantos treinos a mais o atleta deseja visualizar: '))

print()
print('O total de treinos exibidos foram de {}'.format(tot))
print('fim da execução')