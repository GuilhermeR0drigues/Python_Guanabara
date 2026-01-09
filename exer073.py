times = ('Athletico-PR','Atlético-MG','Bahia','Botafogo','Bragantino','Chapecoense','Corinthians','Coritiba','Cruzeiro','Flamengo','fluminense','Grêmio','Internacional','Mirassol','Palmeiras','Remo','Santos','São Paulo','Vasco','Vitória')

print('TABELA DO BRASILEIRÃO')
print('-=-'*12)
#A
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=-'*12)
#B
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('-=-'*12)
#C
print('Os times em ordem alfabeticas ficam posicionados assim: ',sorted(times))
print('-=-'*12)
#D
print(f'A Chapecoense esta na posição ', end='')
print(times.index('Chapecoense') + 1)