player = {'name': 0,
           'nop': 0,
           'goals': 0,
           'total': 0}
goals = list()
players= list()
g1 = 0

while True:
    print('_'*30)
    player['name'] = str(input('Name: '))
    player['nop'] = int(input('Number of partys: '))
    for c in range(0,player['nop']):
        g = goals.append(int(input(f'Goals of {c+1}° party: ')))
    player['goals'] = goals[:]

    for n in goals:
        g1 += n
    player['total'] = g1

    players.append(player.copy())
    g1 = g1-g1
    goals.clear()

    yn = str(input('Do you want continue? y/n:')).strip().upper()[0]
    if yn == 'N':
        break

print('=-'*30)
print('cod      name           goals          total')
print('_'*50)
for c1 in range(0,len(players)):
        print(f'{c1}       {players[c1]["name"]}            {players[c1]["goals"]}          {players[c1]["total"]} ')

while True:
    c2 = int(input('Type the cod for player: [999 for STOP]: '))
    if c2 == 999:
        print('Finalized!')
        break
    elif c2 not in range(0,len(players)):
        print('Error, press the correct code!')
    else:
        print(f'The player {players[c2]["name"]}:')
        for i, v in enumerate(players[c2]["goals"]):
            print(f'The play {i} was {v}')