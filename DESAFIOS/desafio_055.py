#programa para ler o peso das pessoas.
maiorpeso = 0
menorpeso = 0
for cont in range(1, 5 + 1):
    peso = float(input('{}° digite seu peso: '.format(cont)))
    
    if peso > maiorpeso:
        maiorpeso = peso
        
    if cont == 1:
        menorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
        
print('{}kg é o maior peso.'.format(maiorpeso))
print('{}kg é o menor peso.'.format(menorpeso))
        

