
n = int(input("Digite um número: "))
c = n
f = 1
print(f'{n}! = ', end='')
for i in range (n - 1, -1, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
'''
n = int(input("Digite um número: "))
c = n
f = 1
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
'''