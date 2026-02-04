media_da_turma = 0.0
lista_alunos = []
lista_medias = []

aprovados = 0
reprovados = 0
recuperacao = 0

# Média mínima
while True:
    media_minima = float(input('Qual a nota mínima? (Mínimo 3): ').replace(',', '.'))
    if media_minima < 3:
        print('Média mínima inválida... Digite uma média de no mínimo 3!')
    else:
        break

tamanho_da_turma = int(input('Qual o tamanho da turma: '))

# Função para pedir peso 
def pedir_peso(label):
    while True:
        try:

            valor = input(f'Digite o peso da {label}: ').replace(',', '.')
            return float(valor)
        except ValueError:
            print('ERRO: Por favor digite um peso válido.')

peso1 = pedir_peso('Ac1')
peso2 = pedir_peso('Ac2')
peso3 = pedir_peso('AG')
peso4 = pedir_peso('AF')

# Soma dos pesos 
soma_pesos = peso1 + peso2 + peso3 + peso4

i = 0
while i < tamanho_da_turma:
    nome = str(input(f'\nNome do aluno {i+1}: '))
    lista_alunos.append(nome)

# Função para pedir nota
    def pedir_nota(label):
        while True:
            try:
                entrada = input(f'Digite sua nota da {label}: ').replace(',', '.')
                nota = float(entrada)
                if 0 <= nota <= 10: 
                    return nota
                else:
                    print("Erro: A nota deve estar entre 0 e 10.")
            except ValueError:
                print('Erro: Por favor, digite um número válido.')

    n1 = pedir_nota('Ac1')
    n2 = pedir_nota('Ac2')
    n3 = pedir_nota('AG')
    n4 = pedir_nota('AF')

    # Cálculo da média ponderada
    media_aluno = (n1 * peso1 + n2 * peso2 + n3 * peso3 + n4 * peso4) / soma_pesos
    lista_medias.append(media_aluno)
    
    nota_maxima = 10.0 

    print('-'*30)
    print(f'{"NOTAS":^30}')
    print('-'*30)
    print(f'Média Final: {media_aluno:.2f}')
    print('RESULTADO: ', end='')

    # Verificação de resultado aprovação
    if media_aluno <= media_minima - 2:
        print('REPROVADO')
        reprovados += 1
    elif media_aluno < media_minima:
        print('RECUPERAÇÃO (Estude mais!)')
        recuperacao += 1
    elif media_aluno == nota_maxima:
        print('NOTA MÁXIMA, PARABÉNS!')
        aprovados += 1
    else:
        print('APROVADO!')
        aprovados += 1

    i += 1
    
    # Conferencia do Tamanho da Turma
    if i >= tamanho_da_turma:
        break
        
    escolha = input('Deseja fazer mais cadastros? [S/n]: ').strip().lower()
    if escolha == 'n':
        break

# Relatório
print('\n' + '-'*30)
print(f'{"LISTAGEM COMPLETA":^30}')
print('-'*30)

for j in range(len(lista_alunos)):
    print(f'O aluno {lista_alunos[j]:<15} | Média = {lista_medias[j]:.2f}')

print('-'*30)
print(f'{"ESTATÍSTICAS":^30}')
print('-'*30)

# CORREÇÃO: Verificando se a lista não está vazia para evitar divisão por zero
if len(lista_alunos) > 0:
    total = len(lista_alunos)
    perc_aprovados = (aprovados * 100) / total
    perc_reprovados = (reprovados * 100) / total
    perc_recuperacao = (recuperacao * 100) / total

    print(f'Média geral da turma: {sum(lista_medias) / total:.2f}')
    print(f'Aprovados:    {perc_aprovados:.1f}%')
    print(f'Recuperação:  {perc_recuperacao:.1f}%')
    print(f'Reprovados:   {perc_reprovados:.1f}%')
    
