horario = [[08:00], [08:30],]
nomes = []
telefone = []

while True:
    nomes = str(input('Digite seu nome: '))
    telefone = int(input('Digite seu telefone: '))
    horario = str(input('Qual horário você gostaria: '))
    if horario in horario:
        print('HORÁRIO INDISPONÍVEL')
        print('Trabalhamos das 08:00 as 19:00')
        print('Os horarios INDISPONÍVEIS sao os seguintes')
        print(f'{telefone}')
    else:
        break
print('-=' * 30)
print(f'Seu horario esta marcado(a) {nomes} as {horario}')

    