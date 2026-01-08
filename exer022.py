nome = str(input('Digite seu nome completo: ')).strip()


print(f'Seu nome em maiusculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')

new = nome.split()
print(f'Seu primeiro nome tem {len(new[0])} letras' )
