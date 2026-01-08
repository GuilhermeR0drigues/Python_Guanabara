valor_casa = float(input('Qual o valor da CASA? R$'))
salario = float(input('Qual o seu SALARIO? R$'))
tempo = float(input('Em quantos anos vc vai pagar? '))
prestacao_mensal = valor_casa / (tempo * 12)


print(f'Para pagar uma casa de R${valor_casa} em {tempo} a prestação será de {prestacao_mensal:.2f}')

if prestacao_mensal <= salario - (salario * 30/100):
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')