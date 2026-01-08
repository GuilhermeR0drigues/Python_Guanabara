velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('VOCÊ PASSOU DO LIMITE PERMITIDO')
    print(f'VOCÊ IRA PAGAR R${(velocidade - 80) * 7}')
else:
    print('OK PROSSIGA SUA VIAGEM')