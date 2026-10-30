# Crie um programa onde o usário digite uma expresão qualquer, e seu aplicativo deverá analisar se a expressão passada está com os paraenteses e fechados na ordem correta.

abre = 0  # criamos uma variavel para receber o'(' somarmos + 1 e ')' subtrairmos -1 
expressao = []
erro = False
expressao = str(input('Digite a expressão: ')) # aqui a gente coloca as strings dentro da lista

for v in expressao: # aqui criamos o for para percorrer cada caractere da expressão, um de cada vez. a variável V recebe o caractere atual em cada repetição.
      
    if v == '(':    # aqui perguntamos se a condição é verdadeira, se for adicionamos  
        abre += 1
    if v == ')':    # aqui verificamos se a condição é verdadeira e subtraimos
        abre -= 1
    if abre < 0:    # uma das partes mais importantes, perguntamos se o contador fiocou a baixo de zero
        erro = True # precisamos dessa variavel porque o contador pode voltar a zero posteriormente mesmo que a expressão esteja errada
   
if abre == 0 and erro == False: # aqui usamos o operdor lógico and ele exige que as duas condições sejam verdadeiras. abre == 0: não existem parenteses abertos sem fechamento / erro == false: não encontramos fechamento antes da abertura.
    
    print('Essa expressão está certa.')
else:
    print('Essa expressão está errada.')
        