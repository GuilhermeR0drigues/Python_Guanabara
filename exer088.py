from random import randint
from time import sleep
lista = []
jogos = []
total = 1

print('-'*40)
print(f'{'JOGO DA MEGA SENA':^40}')
print('-'*40)

numeros_de_jogos = int(input('Quantos jogos você quer que eu sortei? '))

while total <= numeros_de_jogos:
    count = 0 
    while True:
        num = randint (1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-='*5, end='')
print(f' SORTEANDO {numeros_de_jogos} JOGOS ', end='')
print('-='*5)
print('')

for i, l in enumerate (jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('-='*5, end='')
print(f' < BOA SORTE! > ', end='')
print('-='*5)