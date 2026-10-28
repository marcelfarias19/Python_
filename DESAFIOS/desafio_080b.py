#reforço do exercício 080 (digitar 5 valores e falar as posições)
lista = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))  # foi criada a variável para receber os valores
    if cont == 0 :      
        lista.append(n)  # o primeiro valor ele apenas recebe o valor sem especificar posição.
    elif n > lista[-1]:  # se o valor for maior que o último elemento ele adicionao valorn na ultima posição
        lista.append(n)  # adiona na ultima posição o valor com o .append()
        print('Adicionado ao final da lista da lista')    
    else:       # para descobrir a posição dos outrso vetores é necessário varrer as posições.
        pos = 0 # variavel criada para a posição.
        while pos < len(lista): # enquanto a posição for menor que o tamanho da lista(len(lista)) 
            if n <= lista[pos]: # se a variável n na posição 0 for menor ou igual a lista ele inseri em um posição espeicfica.
                lista.insert(pos, n) # em vez de usar o .append() para inserir você usa o .insert() porque ele inseri entre as posições 
                print(f'Adicionado na posição {pos}')   
                break # depois break para quebrar o laço.
            pos += 1  # esse pos é a variável de controle para o laço não ser infinito e passara próxima posição.
print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')
        