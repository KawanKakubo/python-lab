print('=' * 30)
print(f'{'BANCO':^30}')
print('=' * 30)
valorsaque = int(input("Digite o valor a ser sacado: R$"))
total = valorsaque
totced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R${ced:.2f}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
