salario = float(input('Qual é salário do funcionario? R$'))

if salario <= 1200:
    salario_novo = salario + (salario * (15/100))
    print(f'Quem ganhava R${salario} passa a ganhar R${salario_novo}')
else:
    salario_novo = salario + (salario * (10/100))
    print(f'Quem ganhava R${salario} passa a ganhar R${salario_novo}') 
print('Parabens pela promoção')