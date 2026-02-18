time  = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    total_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range (0,total_partidas):
        partidas.append(int(input(f'Quantos gols o {jogador["Nome"]} fez na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar?[S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if opcao == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys ():
    print(f'{i:<15}',end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca = int(input('Buscar dado de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse codigo {busca}')
    else:
        print(f' -- LEVATAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate[time[busca]["Nome"]]:
            print(f'    No jogo {i} fez {g} gols.')