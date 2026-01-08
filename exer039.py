from datetime import date
atual = date.today().year

nascimento = int(input('Ano de nascimento: '))

idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} em 2025')

if idade == 18:
    print("Chegou a hora do alistamento")
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {atual + (18 -idade)}')
else:
    print('Ja passou da hora de você se alistar né...')