algo = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(algo))

print('Só tem espaços? ', algo.isspace())
print('é um numero? ', algo.isnumeric())
print('Esta em maiusculo? ', algo.isupper())
print('Esta em minusculo? ', algo.islower())
print('É alfabetico? ', algo.isalpha())
print('É alfanumerico? ', algo.isalnum())
print('Esta capitalizada?', algo.istitle())
