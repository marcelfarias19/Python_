#crie um programa que leia 2 valores e mostre o menu na tela.

num1 = int(input('Digie o primeiro valor: '))
num2 = int(input('Digite o segundo valor: ')) 

opcao = 0
while opcao != 5: 
    
    print(''''--MENU ESCOLHA--
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    print()
    opcao = int(input('Digite a opção: '))
    print()   
    
    if opcao == 1:
        somar = num1 + num2
        print('o resultado da soma entre {} e {} é {}'.format(num1, num2, somar)) 
        print()      
                 
    elif opcao == 2:
        mult = num1 * num2
        print('O resultado da multiplicação entre {} e {} é {}'.format(num1, num2, mult))
        print()                       
        
    elif opcao == 3:
        
        if num1 > num2:
            print('O número maior é {}'.format(num1))
            print()
        elif num2 > num1:
            print('O número maior é {}'.format(num2))
            print()
        elif num1 == num2:
            print('os números {} e {} são iguais'.format(num1, num2)) 
            print() 
    
    elif opcao == 4:
        num1 = int(input('Digie o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        print()                 
        
    elif opcao == 5:
        print('Programa encerrado.')