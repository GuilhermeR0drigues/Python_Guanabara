import random

num = random.randint(0,5)

num1 = int(input('A maquina esta pensando em um numero de 0 a 5, tente adivinhar: '))

if num1 == num:
    print(f'Parabens vc acertou, vc escolheu {num1} e a maquina escolheu {num}')
else: 
    print(f'Putzz vc errou, vc escolheu {num1} e a maquina escolheu {num}')