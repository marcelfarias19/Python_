# Tarefa fazer tabuada versão 3

while True: 
    print('=-'*15)
    print('--PROGRAMA DE TABUADA--')
    print('=-'*15)
       
    tab = int(input('Quer ver a tabuada de qual valor: '))
    if tab < 0:
        break
        
    for  cont in range(1, 11):       
        result = tab * cont
        print(f'{tab} x {cont} = {result}') 
    
print()
print('Programa tabuada encerrada! Volte sempre')

        