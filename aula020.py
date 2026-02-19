'''
def mostrarLinha():
    print('--------------------')

mostrarLinha()
print(f'{"CORINTHIANS":^20}')
mostrarLinha()
mostrarLinha()
print(f'{"PORCO":^20}')
mostrarLinha()
mostrarLinha()
print(f'{"BIXARADA":^20}')
mostrarLinha()
'''
def tabela (msg):
    print('-'*20)
    print(msg)
    print('-'*20)


tabela('SCCP')
tabela('Porco')
tabela('trikas')


def sum( a, b):
    c = a + b
    print(f'o valor da soma é {c}')
    

sum(2, 2)
sum(4, 4)
sum(6, 6)


def dobra(lst):
    pos = 0
    while pos <  len(lst):
        lst[pos]*= 2
        pos+=1


valores = [1, 2, 3, 4]
dobra(valores)
print(valores)