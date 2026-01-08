nome = input('Qual o seu nome: ')
salario = float(input('Qual o valor do seu salário: '))

promocao = salario + (salario * (15/100))

print('PARABÉNS {}, voçê ganhou um aumento e ganhará R${}'.format(nome, salario + promocao))