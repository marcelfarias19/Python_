#programa para aplicar multa de velocidade.

vel = int(input('Digite a velocidade com qual o carro passou: '))

if vel > 80:
    multa = float((vel - 80) * 7)
    print('Sua velocidade foi de {} km/h e você foi multado em R$ {:.2f}'.format( vel, multa))
else:
    print("tudo Normal.")   

    