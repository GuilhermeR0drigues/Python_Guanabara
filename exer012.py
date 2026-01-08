nome = input('Digite o nome do produto: ')
preço = float(input('Digite seu valor R$'))

desconto = preço - (preço * (5/100))

print('SUPER DESCONTO, {} de R${:.2f} para R${:.2f}'.format(nome, preço, desconto))