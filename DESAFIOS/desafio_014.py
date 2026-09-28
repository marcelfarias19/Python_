print('=' * 30)
print('CONVERSOR DE TEMPERATURA')
print('=' * 30)

temp = float(input('Informe a temperatura em celsius: '))
far = ((temp * 9 )/ 5) + 32
print('A temperatura de {} C° corresponde a {}°F'.format(temp, far))