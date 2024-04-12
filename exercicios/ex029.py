v = int(input('Digite a velocidade de um carro em km/h: '))
if v >= 80:
    m = (v - 80) * 7
    print(f'Você foi multado no valor de {m} reais.')
else:
    print('Você está dirigindo com prudência, parabéns!')
