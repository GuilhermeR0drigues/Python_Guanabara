lista = list()
par = list()
impar = list()

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    escolha = str(input('Você quer continuar? [S/N]'))
    if escolha in 'Nn':
        break
    
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')   

