def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno equivale à {a}.')


print('Calculadora da área de um terreno retangular')
l = float(input("Digite a largura do terreno: "))
c = float(input("Digite a comprimento do terreno: "))
area(l, c)
