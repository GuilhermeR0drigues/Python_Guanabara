count = 0
soma = 0
num = 0
num = int(input('Digite um numero [999 para para]: '))

while num != 999:
    count += 1
    soma += num
    num = int(input('Digite um numero [999 para para]: '))
    
print(f'Você digitou {count} números e a soma entre eles foi {soma}')
