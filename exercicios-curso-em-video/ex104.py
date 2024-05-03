def leiaInt(msg):
    num = input(msg)
    while num.isnumeric() == False:
        print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        num = input(msg)
    print(f'Você acabou de digitar o número {num}.')


n = leiaInt('Digite um número: ')
