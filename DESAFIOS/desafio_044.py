#valor de produto

produto = float(input('Digite o valor do produto R$: '))
print('--Forma de pagamento-- \n [1] á vista dinheiro / cheque : 10% Desconto. \n [2] á vista no cartão : 5% De desconto. \n [3] em até 2 vezes no cartão preço normal. \n [4] Em 3 vezes no cartão: 20% De juros.  ')
pagamento = int(input('Digite aqui sua opção: '))

if pagamento == 1:
    resultado = produto * 0.90
    print('[1] o valor do seu produto é de R$ {:.2f}'.format(resultado))
elif pagamento == 2:
    resultado = produto * 0.95
    print('[2] o valor do seu produto é de R$ {:.2f}'.format(resultado))
elif pagamento == 3:
    print ('[3] o valor do seu produto é de R$ {:.2f}'.format(produto))
elif pagamento == 4:
    resultado = produto * 1.20
    print('[4] o valor do seu produto é de R$ {:.2f}'.format(resultado))
else:
    print('Opção inválida de pagamento, tente novamente.')
    

    