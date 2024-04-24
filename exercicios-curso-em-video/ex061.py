a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
a10 = a1 + (10 - 1) * r
termos = a1

print('Os 10 primeiros termos dessa PA: ')
print(f'{a1}; ', end='')
while termos < a10:
    termos += r
    print(f'{termos}; ', end='')

print(' ...', end='')