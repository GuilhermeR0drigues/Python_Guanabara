import random

nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite um nome: '))
nome3 = str(input('Digite um nome: '))
nome4 = str(input('Digite um nome: '))

alunos = [nome1, nome2, nome3, nome4]

escolha = random.choice(alunos)
print(f'O aluno que ira apagr a lousa é o {escolha}')