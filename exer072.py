
num = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
    'dezoito', 'dezenove', 'vinte'
)

while True:
    num_pessoa = int(input('Digite um número entre 0 e 20: '))
    
    # Verifica se o número está no intervalo correto
    if 0 <= num_pessoa <= 20:
        break  # Sai do loop se o número for válido
    
    print('Tente novamente. ', end='')

# 3. Exibição do resultado
print(f'Você digitou o número {num[num_pessoa]}')