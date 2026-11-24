# Função

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        
valores = [2, 9, 4, 3, 4, 6]
dobra(valores)
print(valores)