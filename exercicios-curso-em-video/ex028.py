import random
l = [0,1,2,3,4,5]
n = random.choice(l)
x1 = int(input('Tente descobrir um número de 0 à 5: '))
if x1 == n:
    print(f'Parabéns, você acertou o número {n}.')
else:
    print(f'Você errou, que pena, o número escolhido era o {n}. =(')
