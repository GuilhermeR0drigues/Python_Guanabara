boletim = []
count = 0

while True:
    nome = str(input('NOME: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])
    count += 1

    escolha = input('Quer continuar? [S/N] ')
    if escolha in 'Nn':
        break

print(f'\n{boletim}')

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*28)

for i, a in enumerate(boletim):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

while True:
    print('-'*35)
    opcao = int(input('Mostrar notas de qual aluno? ((999)interrompe programa): '))
    if opcao == 999:
        print('FINALIZANDO O PROGRAMA...')
        break
    if opcao <= len(boletim) - 1:
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')

