nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))

media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')

if media < 5:
    print('REPROVADO')
elif media > 7: 
    print('APROVADO')
else: 
    print('RECUPERAÇÃO')