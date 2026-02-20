def area(larg,comp):
    area_terreno = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area_terreno}m²')



print('  Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
