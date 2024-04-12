while True:
    n = int(input("Quer ver a tabuada de qual valor [valores negativos para finalizar]? "))
    if n < 0:
        print('Finalizando o programa!')
        break
    print('-'*20)
    print(f'{n} * 1 = ', n * 1)
    print(f'{n} * 2 = ', n * 2)
    print(f'{n} * 3 = ', n * 3)
    print(f'{n} * 4 = ', n * 4)
    print(f'{n} * 5 = ', n * 5)
    print(f'{n} * 6 = ', n * 6)
    print(f'{n} * 7 = ', n * 7)
    print(f'{n} * 8 = ', n * 8)
    print(f'{n} * 9 = ', n * 9)
    print(f'{n} * 10 = ', n * 10)
    print('-' * 20)
print('Programa encerrado!')
