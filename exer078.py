valores = list()
maior = 0
menor = 0 
for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

print('=-=' *30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor foi o {maior} nas posições ', end='')
for i,c in enumerate(valores):
    if c == maior:
        print(f'{i}...',end='')
print()

print(f'O menor valor foi {menor} nas posições ',end='')
for i,c in enumerate(valores):
    if c == menor:
        print(f'{i}...')
print()