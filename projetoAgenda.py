horarios_disponiveis = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', 
'11:00', '11:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', 
'16:00', '16:30','17:00', '17:30', '18:00', '18:30', '19:00']

nomes = []
telefone = []
agenda_final = []
cadastro = []
while True:
    
    n = str(input('Digite seu nome: '))

    t = int(input('Digite seu telefone: '))

    horario_escolido = str(input('Qual horário você gostaria: '))

    if horario_escolido in horarios_disponiveis:
        cadastro = f' {n} {t}  {horario_escolido}'
        agenda_final.append(cadastro)
        horarios_disponiveis.remove(horario_escolido)
    else:
        print('-='*20)
        print('HORÁRIO INDISPONÍVEL')
        print('Trabalhamos das 08:00 as 19:00')
        print('Os horarios INDISPONÍVEIS sao os seguintes')

    escolha = str(input('Quer continuar? [S/n]')).upper().strip()
    if escolha == 'N':
        break

print('-=' *30)
print(f'Seu horario esta marcado(a) {n} as {horario_escolido}')
print('-=' *30)

for item in agenda_final:
    print(item)
    print('-='*15)




    

    
