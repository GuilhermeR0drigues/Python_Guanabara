matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_dos_pares = maior = soma_das_colunas = 0
for l in range(0,3):
    for c in range(0,3):
        matriz [l][c] = int(input(f'Digite um numero na posição [{l},{c}]: '))
        if matriz [l][c]  % 2 == 0:
            soma_dos_pares += matriz[l][c]
            
print('-='*30)
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
print('-='*30)

#A
print(f'A soma dos pares é {soma_dos_pares}')

#B
for l in range(0,3):
    soma_das_colunas += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_das_colunas}')

#C
for c in range(0,3):
    if c == 0:
        maior = matriz [1][c]
    elif matriz [1][c] > maior:
        maior = matriz[1][c]
print(f'O Maior Número da Segunda Linha é {maior}')