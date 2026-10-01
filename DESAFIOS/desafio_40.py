#Média de notas
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua nota foi {} você foi Reprovado.'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua nota foi {} você está de Recuperação'.format(media))
elif media >= 7:
    print('Sua nota foi de {} Parabéns você foi Aprovado.'.format(media))
