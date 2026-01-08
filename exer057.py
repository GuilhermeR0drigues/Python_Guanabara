sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe o sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')