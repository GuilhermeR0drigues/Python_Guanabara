tot18 = 0
totH = 0
totM20 = 0
total = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F] ')).strip().upper() [0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper() [0]

    if sexo == 'M':
        totH += 1

    if idade >= 18:
        tot18 += 1

    if sexo == 'F' and idade < 20:
        totM20 += 1

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper() [0]


    if opcao == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de mulheres cadastradas: {totM20}')
