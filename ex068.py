from random import choice

escn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont = 0
print('=-'*6)
print('PAR OU ÍMPAR')
print('-='*6)
while True:
    pcn = choice(escn)
    usern = int(input("Digite um número de 0 à 10: "))
    userpoui = str(input("Par ou Impar [P/I]? "))
    print('--'*6)
    soman = usern + pcn

    if userpoui in 'Pp':
        pcpoui = 'I'
        if soman % 2 == 0:
            print('Usuário GANHOU!')
            print(f'O jogador jogou {usern} e o computador {pcn}. Total = {soman}. Deu PAR!')
            print('--' * 6)
            cont += 1
        else:
            print('Você PERDEU!')
            print(f'O jogador jogou {usern} e o computador {pcn}. Total = {soman}. Deu ÍMPAR!')
            print('--' * 6)
            break
    else:
        pcpoui = 'P'
        if soman % 2 == 1:
            print('Usuário PERDEU!')
            print(f'O jogador jogou {usern} e o computador {pcn}. Total = {soman}. Deu ÍMPAR!')
            print('--' * 6)
            break
        else:
            print('Usuário GANHOU!')
            print(f'O jogador jogou {usern} e o computador {pcn}. Total = {soman}. Deu ÍMPAR!')
            print('--' * 6)
            cont += 1
print(f'O número de vitórias consecutivas foi de: {cont}.')
