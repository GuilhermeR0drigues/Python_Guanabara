frase = str(input('Digite uma frase: ')).strip()

print(f'A letra A aprece {frase.lower().count('a')} vezes na frase')

print(f'A primeira letra A apareceu na posição {frase.lower().find('a') +1}')

print(f'A ultima letra A apareceu na posição {frase.lower().rfind('a')+1}')