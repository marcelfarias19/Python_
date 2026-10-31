# Crie um programa onde o usário digite uma expresão qualquer, e seu aplicativo deverá analisar se a expressão passada está com os paraenteses e fechados na ordem correta.

expressao = []
abre = 0
error = False
expressao = str(input('Digite uma expressão: '))
for v in expressao:
    if v == '[':
        abre = abre + 1
    if v == ']':
        abre = abre - 1
    if abre < 0:
        error = True
if abre == 0 and error == False:
    print('Essa expressão está certa.')
else:
    print('Essa exporesão está errada.')