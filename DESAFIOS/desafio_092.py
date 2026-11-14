# Crie um programa que leia um nome, ano de nascimento e carteira de trabalho e cadastre-os ( com idade em dicionário) se por acaso o CTPS for diferente de zero, o dicionário receberá tambem o ano de contratação e o salário. calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
dados = {}
aposentadoria = 0
dados['nome'] = str(input('Nome: '))
dados['ano de nascimento'] = int(input('Ano de nascimento: '))
dados['carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): ')) 
while dados['carteira de trabalho'] != 0:      
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    aposentadoria = (dados['ano de contratação'] - dados['ano de nascimento'] + 35)
    dados['aposentadoria'] = aposentadoria
    print('-=' * 30)
    print(dados)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')       
    break
print('-=' * 30)     


    
