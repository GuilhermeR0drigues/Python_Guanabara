real = int(input('Quantos reias você tem? '))
dolar = int( real / 3.27)

print('Com R${:.2f}, você pode comprar US${:.2f} dolares'.format(real, dolar))