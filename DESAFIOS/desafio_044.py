#valor de produto

produto = float(input('Digite o valor do produto: '))
pagamento = int(input('--Forma de pagamento-- \n [1] á vista dinheiro / cheque : 10% Desconto. \n [2] á vista no cartão : 5% De desconto. \n [3] em até 2 vezes no cartão preço normal. \n [4] Em 3 vezes no cartão: 20% De juros.  '))

if pagamento == 1:
    resultado = produto * .90
    print('[1] opção: o valor do seu produto é de R$ {:.2f}'.format(resultado))
elif pagamento == 2:
    resultado = produto * 0.95
    print('[2] opção: o valor do seu produto é de R$ {:.2f}'.format(resultado))
elif pagamento == 3:
    print ('[3] opção: o valor do seu produto é de R$ {:.2f}'.format(produto))
elif pagamento == 4:
    resultado = produto * 1.20
    print('[4] opção: o valor do seu produto é de R$ {:.2f}'.format(resultado))
    

    