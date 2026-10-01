nome = str(input('Qual é o seu nome? '))
if nome == 'Marcel':
    print('que nome lindo')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino você tem!')
else:
    print('seu nome é bem normal!') 
print('tenha um bom dia {}'.format(nome)) 