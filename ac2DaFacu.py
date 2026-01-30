media_da_turma = 0.0
lista_alunos = []
lista_medias = []

aprovados = 0
aprovados_com_exelecia = 0
reprovados = 0
recuperacao = 0

while True:
    media_minima = float(input('Qual a nota minima? (Naão pode ser menor de 3): '))

    if media_minima < 3:
        print('Média mínima inválida...')
        print('Digite uma média de no mínimo 3!')
    else:
        break

peso1 = float(input('Digite o peso da Ac1: '))
peso2 = float(input('Digite o peso da Ac2: '))
peso3 = float(input('Digite o peso da AG: '))
peso4 = float(input('Digite o peso da AF: '))

tamanho_da_turma = int(input('Qual o tamanho da truma: '))

i = 0
escolha = 'sS'

while (i < tamanho_da_turma):

    nome = str(input('Digite seu nome: '))
    lista_alunos.append(nome)
    i += 1

    n1 = float(input('Digite sua nota da Ac1: '))
    n2 = float(input('Digite sua nota da Ac2: '))
    n3 = float(input('Digite sua nota da AG: '))
    n4 = float(input('Digite sua nota da AF: '))

    nota1 = n1 * peso1
    nota2 = n2 * peso2
    nota3 = n3 * peso3
    nota4 = n4 * peso4
    notaMaxima = 10 * (peso1 + peso2 + peso3 + peso4)

    media_aluno = nota1 + nota2 + nota3 + nota4
    lista_medias.append(media_aluno)

    print('-'*30)
    print(f'{'NOTAS':^30}')
    print('-'*30)
    print(f'Prova 1: Nota: {n1}')
    print(f'Prova 2: Nota: {n2}')
    print(f'Prova 3: Nota: {n3}')
    print(f'Prova 4: Nota: {n4}')
    print('RESULTADO:',end='')

    if  media_minima - 2 >= media_aluno:
        print(f'REPROVADO')
        print(f'nota:{media_aluno:2f}')
        reprovados +=1

    elif media_minima > media_aluno:
        print(f'RECUPERAÇÃO')
        print(f'nota:{media_aluno:2f}')
        print('Estude mais')
        recuperacao += 1

    elif media_minima == media_aluno:
        print('UFAAAA.... essa foi por pouco, APROVADO!')
        print(f'Você e sua nota são {media_aluno}')
        aprovados += 1

    elif media_aluno == notaMaxima:
        print('NOTA MÁXIMA, PARABÉNS!')
        print(f'nota:{media_aluno}')
        aprovados_com_exelecia += 1
    else:
        print('aprovado!')
        aprovados += 1
    if tamanho_da_turma == i:
        break
    escolha =(str(input('Deseja fazer mais cadastros? [S/n]')))

    if escolha in 'nN':
        break

print('-'*30)
print(f'{'LISTAGEM COMPLETA':^30}')
print('-'*30)
print('')

for j in  range(len(lista_alunos)):
    print(f'O aluno {lista_alunos[j]} tem a média = {lista_medias[j]}')
    j+= 1
print('-'*30)
print(f'A media da turma foi {sum(lista_medias) / len(lista_alunos)}')
print('')
print(f'foram {aprovados_com_exelecia*100 / tamanho_da_turma}% da turma foram aprovados com exelência')
print('')
print(f'{aprovados_com_exelecia*100 / tamanho_da_turma}% da turma ficou em recuperação')
print('')
print(f'foram {aprovados_com_exelecia*100 / tamanho_da_turma}% aprovados sem ser com a nota máxima')
print('')
print(f'{aprovados_com_exelecia*100 / tamanho_da_turma}% Repetiram')