numeros =(int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um  número: ')),
            int(input('Digite o último número: '))) 

print(f'Você digitou os valores: {numeros}')

#A
print(f'O número (9) apareceu {numeros.count(9)}')
#B
print(f'O número (3) apareceu na posição {numeros.index(3)}')
#B

par = [n for n in numeros if n % 2 == 0]

print(f'Os numeros PARES que apareceram foram os seguintes: {par}')