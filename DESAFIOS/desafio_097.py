# faça um programa que tenha uma funçãpo chamada 'escreva()' , que receba um texto qualquer como parâmetro e mostre uma mensagem com um tamanho adaptável. 

def escreva(txt):
    tamanho = len(txt) + 4
    print('='* tamanho)
    print(f'  {txt}')
    print('='* tamanho)

# principal programa
escreva('ola mundo!')
escreva('exe')
escreva('o maior número do mundo está aqui!!')
escreva('Marcel neves Farias')