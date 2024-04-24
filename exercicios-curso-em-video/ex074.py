import random
numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
           random.randint(1, 10), random.randint(1, 10))
print('Os números sorteados foram: ', end='')
a = b = 0
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')
