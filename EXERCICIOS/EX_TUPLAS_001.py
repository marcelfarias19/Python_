# exercícios de tuplas.

# Tuplas são imutáveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata-frita')

for comida in lanche:              #aqui o laço mostra todos os valores até terminarem, no fim sai do laço.
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print()

'''print(len(lanche))'''          # aqui o len ele mostra quantos valores tem dentro de lanche.

for cont in range(0, len(lanche)):
    print(f'eu vou comer um {lanche[cont]} na posição {cont}')
print('comi pra caramba1')
print()

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')

