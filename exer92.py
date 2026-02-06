from datetime import datetime
cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - cadastro['idade']
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade'] + (cadastro['contratação'] + 35) - datetime.now().year
    print('-='*30)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor de {v}')
else:
    for k, v in cadastro.items():
        print(f' - {k} tem o valor de {v}')