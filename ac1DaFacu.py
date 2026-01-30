n1 = float(input('Digite sua nota da Ac1: '))
n2 = float(input('Digite sua nota da Ac2: '))
n3 = float(input('Digite sua nota da AG: '))
n4 = float(input('Digite sua nota da AF: '))

nota1 = n1 * 0.15
nota2 = n2 * 0.35
nota3 = n3 * 0.10
nota4 = n4 * 0.40

media = nota1 + nota2 + nota3 + nota4

if media < 5:
    print(f'RECUPERAÇÃO')
    print(f'nota:{media:2f}')
elif media == 5:
    print(f'Você passou por pouco')
    print(f'nota:{media:2f}')
    print('Estude mais')
elif media == 10:
    print('PARABENS, SEMESTRE PERFEITO')
    print(f'Você e sua nota são {media}')
else:
    print('Você está aprovado')
    print(f'nota:{media}')
