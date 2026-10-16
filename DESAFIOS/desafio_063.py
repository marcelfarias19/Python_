#sequencia de fibonacci
print()
print('--SEQUÊNCIA DE FIBONACCI--')
print()
f1 = int(input('Digite um número inteiro: '))
n = int(input('Digite quantas repetições você quer: '))

cont = 1
f3 = 0
f2 = 0
while cont <= n:
    f3 = f2 + f1
    f1 = f2
    f2 = f3
       
    print(f3)    
    cont = cont + 1
print()
print('Fim da execução')