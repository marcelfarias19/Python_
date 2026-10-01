#Programa para aprovar impréstimos
salario = float(input('Qual é o seu salário: '))
emprestimo = float(input('Qual é o valor da casa: '))
parcelas = float(input('Em quantos meses você pretende pagar: '))

prestacao = emprestimo / parcelas

if salario * 0.30 <= prestacao:
    print('O empréstimo foi Negado.')
else:
    print('O empréstimo foi Aprovado.')
    
    
    
    
    