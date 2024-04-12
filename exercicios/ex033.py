n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um outro número: '))
if n1 > n2 > n3:
    print(f'O maior valor é {n1} e o menor {n3}.')
elif n2 > n3 > n1:
    print(f'O maior valor é {n2} e o menor {n1}.')
elif n3 > n2 > n1:
    print(f'O maior valor é {n3} e o menor {n1}.')
elif n1 > n3 > n2:
    print(f'O maior valor é {n1} e o menor {n2}.')
elif n2 > n1 > n3:
    print(f'O maior valor é {n2} e o menor {n3}.')
elif n3 > n1 > n2:
    print(f'O maior valor é {n3} e o menor {n2}.')
