def ficha(jogador='<desconhecido>', golsfeitos=0):
    return f'O jogador {jogador} fez {golsfeitos} gols.'


jog = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jog.strip() == '':
    print(ficha(golsfeitos=gols))
else:
    print(ficha(jog, gols))

