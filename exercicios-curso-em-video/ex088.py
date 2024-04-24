import time, random

jogostotal = []
print('-' * 30)
print('JOGA NA MEGA SENA'.center(30))
print('-' * 30)
njgs = int(input("Quantos jogos vão ser jogados: "))

for c in range(njgs):
    jogo = random.sample(range(1, 61), 6)
    jogostotal.append(jogo)

print(f'\n-=-=-= SORTEANDO {njgs} JOGOS =-=-=-\n'.center(30))
time.sleep(1)

for i, jogo in enumerate(jogostotal):
    print(f'Jogo {i + 1}: {sorted(jogo)}')
    time.sleep(1)

print(f'\n-=-=-=-= < BOA SORTE > =-=-=-=-\n'.center(30))
