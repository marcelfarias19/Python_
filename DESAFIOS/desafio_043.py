#calculo de massa corporal

peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt * alt)
print('Seu imc é {:.2f}.'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade.')
elif imc >= 40:
    print('Você está com obesidade morbida.')