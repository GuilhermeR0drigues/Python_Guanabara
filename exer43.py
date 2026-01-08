peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Com {imc:.2f} você está ABAIXO DO PESO')
elif imc < 25:
    print(f'Com {imc:.2f} você está PESO IDEAL')
elif imc < 30:
    print(f'Com {imc:.2f} você está SOBREPESO')
elif imc > 40:
    print(f'Com {imc:.2f} você está OBESIDADE')
else:
    print(f'Com {imc:.2f} você está OBESIDADE MÓRBIDA')