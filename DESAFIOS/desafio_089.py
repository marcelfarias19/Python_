# Crie um programa que leia nomes e duas notas de vários alunos e guarde tudo em uma lista composta, no final mostre um boletim contando a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 

print('-='*30)
print('>> CADASTRO DE ALUNOS <<'.center(60))
print('-='*30)

dados = list()
lista = []
resp = 'N'
media = 0

while True:
    dados.append(str(input('Nome do aluno: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('nota 2: ')))     
    lista.append(dados[:])
    dados.clear()
    
    resp = str(input('Você deseja continuar: [S/N] ')).upper().strip()    
    if resp == 'N':
        break    

print('-='*40) 
print(f'N° NOME                     MÈDIA')   
for i, c in enumerate(lista):  
    media = (c[1] + c[2]) / 2 
    print(f'{i} {c[0]:.<25} {media:.2f}')
    
print('-')  
      
cont = 0
while cont != 999:  
    cont = int(input('Mostrar notas de qual aluno? (999 interrompe): '))  
    for i, c in enumerate(lista):
        if cont == i:
            print(f'As notas de {c[0]} são {c[1], c[2]} ')
            print('-'*40) 
            
print('FINALIZADO')         
print('>> VOLTE SEMPRE <<'.center(30))
