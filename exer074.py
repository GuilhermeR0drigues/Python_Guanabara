from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), 
       randint(0,10), randint(0,10), )
print(f'Os valores sorteados foram {num}')
print('-=-'*10)
print(f'Omaior valor sorteado foi {max(num)}')
print('-=-'*10)
print(f'O menor valor sorteado foi {min(num)}')

