# Listas parte 2 /  vamos explorar aqui as listas dentro das listas.

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # aqui precisamos criar uma cópia com [:] se não a lista se repete 
teste [0] = 'Maria'
teste [1] = 22
galera.append(teste[:])
print(galera)
