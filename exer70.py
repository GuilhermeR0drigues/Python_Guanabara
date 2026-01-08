valor_total = 0
produto_mais_1000 = 0
qtd_exec_prog = 0

while True:
    print('-' * 27)
    print('  LOJA SUPER BARATÃO  ')
    print('-' * 27)

    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    valor_total += preco

    if qtd_exec_prog == 0:
        produto_barato_nome = nome
        produto_barato_preço = preco
    

    if preco < produto_barato_preço:
        produto_barato_preço = preco
        produto_barato_nome = nome

    if preco >= 1000:
        produto_mais_1000 += 1

    opcao = str(input('Quer continuar? [S/n] ')).upper().strip()  
    

    qtd_exec_prog += 1
    
    if opcao == 'N':
        break

print('----FIM DO PROGRAMA----')
print(f'O total de produtos cadastrados foi de {qtd_exec_prog}')
print(f'O total da compra foi de R${valor_total}')
print(f'Temos {produto_mais_1000} produto custando mais de R$1.000,00')
print(f'O produto mais barato foi {produto_barato_nome} que custa R${produto_barato_preço}')