a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
a10 = a1 + ( 9 * r )
for c in range(a1, a10 + r, r):
    print(f'{c}', end=' -> ')
print('...')