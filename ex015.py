d = int(input('Quantos dias o carro será alugado? '))
km = int(input('Quantos kms foram rodados? '))
p = (60 * d) + (0.15 * km)
print(f'O preço à ser pago pela locação do carro por {d} dias e rodados {km}km são: R${p:.2f}.')
