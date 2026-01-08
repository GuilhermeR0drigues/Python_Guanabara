rodagem = float(input('Quantos Km foram percorridos: '))
dias = int(input('Quantos dias vc usou o carro: '))

preço_dia = dias * 60
preço_rodagem =  rodagem * 0.15

print('Somando R${}(dias) com R${}(quilometragem), você deve pagar R${}'.format(preço_dia, preço_rodagem, preço_rodagem + preço_dia ))