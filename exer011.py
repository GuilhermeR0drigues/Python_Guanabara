lado = float(input('Qual a altura da parede(em metros): '))
altura = float(input('Qual a altura da parede(em metros): '))

area = lado * altura
tinta = area / 2

print('Em uma parede de {}x{}, será necessario {} litros de tinta para {}m² de parede'.format(lado, altura, tinta, area))
