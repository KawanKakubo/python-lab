num = int(input('Informe um número: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000
print(f'Analisando o {num}...')
print(f'Unidade: {u}.')
print(f'Dezena: {d}.')
print(f'Centena: {c}.')
print(f'Unidade de Milhar: {um}.')
