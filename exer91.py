from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
}
ranking = []

print('Valores sorteados: ')
for v, k in jogo.items():
    print(f'{v} tirou {k} no dado.')
    sleep(1)
print('-='*30)
print(f"{'  == RANKING ==  ':^20}")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} {v[1]}pts')