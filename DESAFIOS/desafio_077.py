# criar programa com uma tupla e várias palavras (não usar acento)

tupla = (
    'computador',
    'janela',
    'telefone',
    'caderno',
    'abacaxi',
    'bicicleta',
    'chocolate',
    'ventilador',
    'teclado',
    'mochila'
)

# treinar mais como percorrer pelas variaveis com o for ou while
# não esquecer do end=' ' para não haver a quebra de linha / treinar mais isso

for palavra in tupla:
    print(f'Na palavra {palavra.upper()} temos: ', end=' ')     
    for vogal in palavra:
        if vogal in 'AEIOUaeiou':            
            print(f'{vogal}', end=' ' )
    print()                                           # esse print foi importante para a quebra de linha

    
           
        