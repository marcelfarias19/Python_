#leitor de sexo das pessoas

'''resp = 'S'

while resp == 'S':
    n = str(input('informe seu sexo [M / F]: ')).upper()  
    
    if n == 'M' or n == 'F':
        print('sua escolha foi {}'.format(n))
    else:
        print('Error: Digite novamente')
    
    resp = str(input('deseja continuar [S / N]: ')).upper()'''
    
sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]   
while sexo not in 'M, F':
    sexo = str(input('dados inválidos')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))



    
    

    