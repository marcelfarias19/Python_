# Reforço do exercício de progressão aritmética

print()
print('--PROGRESSÃO ARITMÉTICA--')
print()

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 8
tot = 0
while mais != 0: 
    tot = tot + mais
    while cont <= tot:
        print('{} '.format(termo), end=' ')
        termo = termo + razao             
        cont = cont + 1        
      
    print('PAUSA')        
    mais = int(input('Quantos termos adicionais você gostaria de mostrar? '))

print()        
print('Fim da execução')