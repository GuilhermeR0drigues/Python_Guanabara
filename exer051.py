print('=' * 27)
print('    10 TERMOS DE UMA PA    ')
print('=' * 27)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range (0,10):
    print(f'{termo}' , end=' -> ')
    termo = termo + razao 
print('ACABOU')