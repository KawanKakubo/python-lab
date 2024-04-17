matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
mai = men = soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ] ', end='')
    print()
print('-=-'*30)
print(f'Os valores pares digitados foram: {pares}')
for l in range(0, 3):
    soma += matriz[l][2]
print(f'A soma dos valores da 3° coluna é igual à: {soma}')
for c in range(0, 3):
    if c == 0:
        mai = men = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
    elif matriz[1][c] < men:
        men = matriz[1][c]
print(f'O maior valor da coluna 2 é: {mai}')
print(f'O menor valor da coluna 2 é: {men}')
