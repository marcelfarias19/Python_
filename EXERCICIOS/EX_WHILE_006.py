#exercício que lê uma PA (progressão aritmética)

print()
print('--CONTROLE DE PRODUÇÃO--')
print()

pd1 = int(input('Quantas peças foram produzidas no primeiro dia: '))
pd2 = int(input('Quantas peças a produção aumentará por dia: '))
pd3 = pd1
print()
cont = 1
mais = 6
tot = 0
while mais != 0:  
    tot = tot + mais  
    while cont <= tot:      
        print('dia {}: {} peças  '.format(cont, pd3))
        pd3 = pd3 + pd2          
        cont = cont + 1
        
    print('PAUSA')
    mais = int(input('Quantos dias adicionais deseja mostrar: (0 finaliza a sessão) '))

print('Produção finalizada com {} dias exibidos'.format(tot))
print('Fim da execução')