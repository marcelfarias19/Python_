# Tarefa fazer tabuada versão 3

while True: 
    print('=-'*15)
    print('--PROGRAMA DE TABUADA--')
    print('=-'*15)
       
    tab = int(input('Quer ver a tabuada de qual valor: '))    
    for  cont in range(1, 11):       
        result = tab * cont
        print(f'{tab} x {cont} = {result}')
        cont = cont + 1    
        
    if tab < 0:
        break
    
print()
print('fim da execução!')
        