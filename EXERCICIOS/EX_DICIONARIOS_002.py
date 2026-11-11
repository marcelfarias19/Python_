# Exercícios da variável composta { dicionario } laços 

pessoas = {'nome': 'Marshall', 'idade': 40, 'sexo': 'M'}
pessoas['nome'] = 'Lucas' # com esse método você pode substituir o elemento da lista
pessoas['idade'] = 25
pessoas['peso'] = 95 # da mesma forma pode adicionar um elemento, sem precisar de um .append()
for k, v in pessoas.items():   # posso usar esse método no lugar de enumerate.
    print(f'{k} : {v}')