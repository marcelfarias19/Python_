#Programa para ler nome:
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
primeiro_nome = nome.split()[0]
print(len(primeiro_nome))

separado = nome.split()
print('o primeiro nome é {} {} '.format(separado[0]))
print('o segundo nome é {} '.format(separado[1]))

