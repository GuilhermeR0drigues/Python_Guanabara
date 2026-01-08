from random import randint
vitoria = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10) 
    soma = jogador + computador
    tipo = ''

    tipo = str(input('Par ou Ímpar? [P/I]' )).strip().upper() [0]
    
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]' )).strip().upper() [0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if soma % 2 == 0:
            print('Voce VENCEU')
            vitoria += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if soma % 2 == 0:
            print('Você VENCEU')
            vitoria += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')