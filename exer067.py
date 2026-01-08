while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    for tabuada in range(1,11):
        print(f'{num} x {tabuada} = {num*tabuada}')
    if num < 0:
        break
print('FIM!')