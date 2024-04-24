s = int(input('Digite seu salário: '))
if s >= 1250:
    a1 = (s * 0.1) + s
    print(f'Você recebeu um aumento e seu novo salário é: {a1}.')
else:
    a2 = (s * 0.15) + s
    print(f'Você recebeu um aumento e seu novo salário é: {a2}.')
