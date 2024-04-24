numbers = list()
pares = list()
impares = list()
numbers.append(pares)
numbers.append(impares)
cont = 0
while cont != 7:
    n = int(input("Digite um número: "))

    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)

    cont += 1

pares.sort()
impares.sort()

print(f'Lista geral: {numbers}.')
print(f'Lista pares: {pares}.')
print(f'Lista ímpares: {impares}.')