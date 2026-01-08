num = int(input('Qual tabuada você quer? '))
fator = 0

for c in range(0,11):
    print("-=-" *12)
    print(f'{num} x {fator} = {num * fator}')
    fator = fator + 1
