num = int(input('Digite um numero: '))
tot = 0

for c in range(1,num+1):

    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')

    print(f'{c}', end=' ')

print(f'\n\033[mO numero {num} foi divisivel por {tot} vezes ')

if tot == 2:       
    print(f'O {num} é SIM primo')
else:
    print(f'O {num} NÃO é primo')
