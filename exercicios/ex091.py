import random
import time
import operator
jogadores = dict()
print('Valores sorteados:')
for i in range(1,5):
    jogadores[f'Jogador {i}'] = random.randint(1, 6)
for k, v in jogadores.items():
    time.sleep(1)
    print(f'    O {k} tirou: {v}.')
print()
time.sleep(1)
print('Ranking dos jogadores:')
ranking = list()
ranking = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'    {i+1}° Lugar: {v[0]} com {v[1]}.')
