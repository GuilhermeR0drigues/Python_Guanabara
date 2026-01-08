print('===== LOJAS DO GUILHAS =====')

preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/pix')
print('[2] à vista cartão')
print('[3] 2x vista cartão')
print('[4] 3x vista cartão')
escolha = int(input('Qual é a opção? ')) 

if escolha == 1:
    desconto = preço - (preço * 10/100)
    print(f'Sua compra de {preço} vai custar {desconto} no final')
elif escolha == 2:
    desconto = preço - (preço * 5/100)
    print(f'Sua compra de {preço} vai custar {desconto} no final')
elif escolha == 3:
    print(f'Sua compra custou {preço} ')
else:
    desconto = preço + (preço * 20/100)
    print(f'Sua compra de {preço} vai custar {desconto} no final')