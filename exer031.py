distancia = int(input('DIgite a distancia da sua viagem: '))

if distancia <= 200:
    valor = distancia * 0.5
    print(f'Você irá viajar por {distancia}Km.')
    print(f'O preço da sua viagem será de R${valor}')
else:
    valor = distancia * 0.45
    print(f'Você irá viajar por {distancia}Km.')
    print(f'O preço da sua viagem será de R${valor}')