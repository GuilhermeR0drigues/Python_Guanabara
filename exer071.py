print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

saque = int(input('Que valor você quer sacar? R$'))
total = saque

cedula = 50
total_de_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_de_cedula += 1
    else: 
        if total_de_cedula > 0:
            print(f'Total de {total_de_cedula} cedulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_de_cedula = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao banco CEV. Tenha um bom dia')