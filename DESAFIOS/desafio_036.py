#Programa para aprovar impréstimos
salario = float(input('Qual é o seu salário: '))
emprestimo = float(input('Qual é o valor da casa: '))
parcelas = int(input('Em quantos meses você pretende pagar: '))

prestacao = emprestimo / parcelas

print('para pagar uma casa de R${:.2f} em {:.2f} '.format(emprestimo, parcelas))
print('A prestação será de R${} em {} parcelas.'.format(prestacao, parcelas))

if salario * 0.30 <= prestacao:
    print('O empréstimo foi Negado.')
else:
    print('O empréstimo foi Aprovado.')
    
    
    
    
    