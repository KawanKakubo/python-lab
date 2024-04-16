print('SEQUÊNCIA DE FIBONACCI')
n = int(input("Digite a quantidade de termos: "))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3

while cont <= n:
    tx = t1 + t2
    print(f' -> {tx}', end='')
    t1 = t2
    t2 = tx
    cont += 1
print(' FIM')
