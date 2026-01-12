lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    
    escolha = str(input('Quer continuar? [S/N]'))
    if escolha in 'Nn':
        break


print('=-' * 30)

print(f'Você digitou {len(lista)} elementos.')

lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

tem = ''
if 5 in lista:
    tem = print(f'O valor 5 FOI encontrado na lista!')
else:
    tem = print(f'O valor 5 NÃO FOI encontrado na lista!')

