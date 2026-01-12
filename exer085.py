par = []
impar = []

for p in range(0,7):
    numero = int(input(f'Digite o {p + 1}° valor: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print('=-' * 30)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores Ímpares digitados foram: {impar}')