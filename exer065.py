resposta = 'S'
num = count = soma = maior = menor = 0

while resposta in 'Ss':

    num = float(input('Digite um número: '))
    count += 1
    soma += num

    if count == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Quer continuar? [S/N] '))

media = soma / count

print(f'Você digitou {count} números e a média foi {media:.2f})')
print(f'O maior valor foi {maior} e o menor foi {menor}')
