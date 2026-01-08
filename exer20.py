import random 


nome1 = str(input('Aluuno 1: '))
nome2 = str(input('Aluuno 2: '))
nome3 = str(input('Aluuno 3: '))
nome4 = str(input('Aluuno 4: '))

alunos = [nome1, nome2, nome3, nome4]

random.shuffle(alunos)

print(alunos)