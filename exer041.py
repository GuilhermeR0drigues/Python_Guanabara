from datetime import date

atual = date.today().year

nasciemnto = int(input('Digite o ano de nascimento do atleta: '))

idade = atual - nasciemnto

if idade < 10:
    print('MIRIM')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JÚNIOR')
elif idade < 26:
    print('SÊNIOR')
elif idade >= 26:
    print('MASTER')