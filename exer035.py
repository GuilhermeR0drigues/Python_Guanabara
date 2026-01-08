print('-=-'*20)
print('Analisador de Trinângulo')
print('-=-'*20)
ld1 = float(input('Prinmeiro Seguimento: '))
ld2 = float(input('Segundo Seguimento: '))
ld3 = float(input('Terceiro Seguimento: '))

if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld1 + ld2:
     print('Os seguimento acima PODEM FORMAR um trinângulo')
else:
    print("Os seguimentos acima NÃO PODEM FORMAR um triângulo")