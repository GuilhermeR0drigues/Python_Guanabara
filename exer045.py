import random

computador = random.randint(0,2)

print('Suas opções:')
print('[0] PREDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
print('KEN')
print('PO!!!')
print('-=-' * 10)
print(f'computador escolheu {computador}')
print(f'jogador escolheu {jogador}')
print('-=-' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    else:
        print('COMPUTADOR VENCEU')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADOR VENCEU')
else:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('EMPATE')