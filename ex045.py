from random import randint
from time import sleep
itens = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input("Qual sua opção? "))
print('JÔ!')
sleep(1)
print('KÊN!')
sleep(1)
print('PÔ!')
sleep(2)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}.')
print(f'Jogador jogou {itens[jogador]}.')
print('-=' * 11)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
