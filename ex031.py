d = int(input('Digite a distância da viagem em KM: '))
if d <= 200:
    v1 = d/2
    print(f'O valor da passagem será: {v1} reais.')
else:
    v2 = d * 0.45
    print(f'O valor da passagem será: {v2} reais.')
