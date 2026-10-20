# projeto caixa eletrônico

while True:
    print('=-'*20)
    print('== BANCO MARSHALLS ==')
    print('=-'*20)

    valor = int(input('Que valor você deseja sacar: R$  '))
    print('=='*20)
    cedula_50 = valor // 50
    resto_50 = valor % 50
    cedula_20 = resto_50 // 20
    resto_20 = resto_50 % 20 
    cedula_10 = resto_20 // 10
    resto_10 = resto_20 % 10
    cedula_05 = resto_10 // 5
    resto_05 = resto_10 % 5
    cedula_01 = resto_05 // 1
    resto_01 = resto_05 % 1    

    if cedula_50 > 0:
        print(f'Total de {cedula_50} cédulas de R$50')
        
    if cedula_20 > 0:
        print(f'Total de {cedula_20} cédulas de R$20')
        
    if cedula_10 > 0:
        print(f'Total de {cedula_10} cédulas de R$10')
        
    if cedula_05 > 0:
        print(f'Total de {cedula_05} cédulas R$5')
        
    if cedula_01 > 0:
        print(f'Total de {cedula_01} células R$1')    
    
    print()
    resp = str(input('Deseja continuar a operação: [S/N] ')).upper().strip()
    if resp == 'N':
        break  

print()
print('volte sempre ao BANCO MARSHALLS')    