#exercício para treinar o laço de repetição while.

n = 1
num_par = 0
num_imp = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            num_par = num_par + 1
        else:
            num_imp = num_imp + 1
print('Você digitou {} numeros pares e {} numeros impares.'.format(num_par, num_imp))