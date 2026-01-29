horarios_disponiveis = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', 
'11:00', '11:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', 
'16:00', '16:30','17:00', '17:30', '18:00', '18:30', '19:00']

agenda_final = []
cadastro = ''

while True:
    
    n = str(input('Digite seu nome: ')).strip().title()

    # Volta para o topo se houver um erro.
    try:
        t = int(input('Digite seu telefone: '))
    except ValueError:
        print('Erro: Por favor, digite apenas números no telefone.')
        continue 

    horario_escolhido = str(input('Qual horário você gostaria: '))

    # Verifica se tem ou não o horario
    if horario_escolhido in horarios_disponiveis:
        cadastro = f' {n} {t}  {horario_escolhido}'
        agenda_final.append(cadastro)
        horarios_disponiveis.remove(horario_escolhido)

        print('-=' *30)
        print(f'Seu horario esta marcado(a) {n} as {horario_escolhido}')
        print('-=' *30)
    else:
        print('-='*20)
        print('HORÁRIO INDISPONÍVEL')
        print('Trabalhamos das 08:00 as 19:00(pausa para o almoço (12:00-13:00)')
        print('Os horarios DISPONÍVEIS sao os seguintes')
        for i in horarios_disponiveis:
            print(i)

    escolha = str(input('Deseja finalizar o programa? [S/n]')).upper().strip()
    print('')
    if escolha == 'S':
        break

#horarios cadastrados 
for item in agenda_final:
    print(item)
    print('-'*30)

#horario disponivel ainda 
print('='*20)
print('Horáios Disponíveis ')
print('='*20)
for i in horarios_disponiveis:
    print(i)
    print('-'*10)




    
