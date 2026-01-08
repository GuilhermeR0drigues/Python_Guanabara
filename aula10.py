tempo = int(input('Quantos anos tem o seu carro? '))

#SITUAÇÕES SIMPLIFICADAS
# tempo = int(input('Quantos anos tem o seu carro? '))
# print('carro novo' if tempo <=3 else'carro velho')
# print('fim')


if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--fim--')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4)/ 4

if media <5:
    print(f'RECUPERAÇÃO, você tirou {media}')
else: 
    print(f'APROVADO, você tirou {media}')