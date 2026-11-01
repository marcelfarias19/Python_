# Listas parte 2 /  vamos explorar aqui as listas dentro das listas.

galera = list()
dados = list()
totmaior = totmenor = 0

for cont in range(0,5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print('-='*20)
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')