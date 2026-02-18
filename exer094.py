geral = []
pessoa = {}
soma = media = 0 
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    geral.append(pessoa.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda com S ou N.')
    if opcao == 'N':
        break
print('-='*30)


#A 
print(f'A)  Foram cadastradas {len(geral)} pessoas')
#B
media = soma / len(geral)
print(f'B)  A média de idade foi de {media}')
#C
print('C)  As mulheres cadastradas foram: ', end='')
for p in geral:
    if p['sexo'] in 'Ff':
        print(f'\n{p["nome"]}')
#D
print('D)  Lista de pessoas acima da média: ')
for p in geral:
    if p['idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v};',end='' )
        print()
print("<< ENCERRADO >>")