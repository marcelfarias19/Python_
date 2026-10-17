#melhorando o desafio 061
print()
print('--Progressão aritmética--')
print()  

primeiro = int(input('Digite o valor do primeiro termo aritmético: ')) 
razao = int(input('Digite o valor da razão aritmética: '))
termo = primeiro
print()
cont = 1
total = 0
mais = 10
while mais != 0:                                 # fazer mais exercícios como esse 062
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print()    
print('Progressão finalizada com {} termos mostrados'.format(total))
