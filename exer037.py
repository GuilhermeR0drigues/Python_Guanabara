num = int(input('Digie um número interiro: '))
print('Escolha a conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter par OCTAL')
print('[3] converter para HEXADECIMAL')

escolha = int(input('Sua escolha: '))

if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')

elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

elif escolha != 1 or 2 or 3:
    print('OPÇÃO INVALIDA, JEGUE')

else:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

print('-=-' * 15)
print(f'{num} em binario {bin(num)[2:]}, octal {oct(num)[2:]} e hexadecimal {hex(num)[2:]}')
print('-=-' *15)
    