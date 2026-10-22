# exercícios de tuplas.

extenso = ('zero', 'um', 'dois', 'três', 'quatro')

num = int(input('Digite um número entre 0 e 4: '))

while True:
    
    if num < 0 or num > 4:
        num = int(input('tente novamente. digite um número entre 0 e 4: '))
    else:
        print(f'Você digitou o número {extenso[num]}')
        break
        
    
# o que aprendemos com esse exercício: que uma variável pode ser reutilizada dentro de um laço 
# e que você pode guardar a posição dentro de uma tupla dentro de uma variável / tupla[variavel]  
# prestar atenção nos testes lógicos do começo do laço. 

       
   
    
    
    
        
    
    
    
    
    
    


