from random import randint

computer_number = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0
while not acertou:
    jogador= int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computer_number:
        acertou = True
    else:
        if jogador < computer_number:
            print('Mais... Tente mais uma vez.')
        elif jogador > computer_number:
            print('Menos... Tente mais uma vez.')
print(f'Acertou! Você precisou de {palpites} tentativas para adivinhar o número {computer_number}.')