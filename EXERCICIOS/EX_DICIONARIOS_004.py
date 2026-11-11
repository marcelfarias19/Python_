# Exercícios da variável composta { dicionario } 

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # aqui voce não pode usar [:] para o fatiamento então usamos .copy()
print(brasil)

for e in brasil: # aqui ele tira cada estado e coloca em e
    for k, v in e.items(): # aqui ele mostra os items dentro as variáveis
        print(f'O campo {k} tem valor {v}')
print('-' * 30)

for e in brasil:
    for v in e.values():
        print(v, end='  ')
    print()