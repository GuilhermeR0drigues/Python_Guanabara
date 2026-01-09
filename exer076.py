listagem = ('lapis', 1.75,
            'Borracha', 2,
            'Caderno,', 15.90,
            'Estojo', 25,
            'Tranferidor', 4.20,
            'Compasso',  9.99,
            'Mochila', 120.23,
            'Caneta', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{'LISATGEM DE PREÇO':^40}')
print('-'*40)

for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print('-'*40)