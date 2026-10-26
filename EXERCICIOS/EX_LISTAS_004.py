# Exercícios de listas

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8        
# Nas Listas quando você altera a posição de uma altera na outra tambem se estiver conectada 
# Se você não quiser fazer uma ligação basta colocar [:] ex: =>   b = a[:] assim ele não cria uma cópia na lista.

print(f'Lista A: {a}')
print(f'Lista B: {b}')