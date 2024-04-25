info_jogador = dict()
soma_gols = 0
Gols = list()
info_jogador['Nome'] = str(input("Nome do Jogador: "))
qnt_partidas = int(input(f"Quantas partidas {info_jogador['Nome']} jogou? "))
for i in range(1, qnt_partidas+1):
    a = int(input(f"Quantos gols na partida {i}: "))
    Gols.append(a)
info_jogador['Gols'] = Gols
for i, v in enumerate(Gols):
    soma_gols += v
info_jogador['Total de Gols'] = soma_gols
print('=====')
for k, v in info_jogador.items():
    print(f'{k} tem o valor {v}.')
print('=====')
print(f'O jogador {info_jogador['Nome']} jogou {qnt_partidas} partidas.')
for i, v in enumerate(Gols):
    print(f'    Na partida {i+1} fez {v} gols.')
print(f'Foi um total de {info_jogador['Total de Gols']} gols!')