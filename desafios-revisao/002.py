num = input('Digite um número inteiro: ')
if num.isdigit():
    num_int = int(num)
    if num_int % 2 == 0:
        print('O número é par!')
    else:
        print('O número é ímpar!')
else:
    print('Isso não é um número inteiro.')
