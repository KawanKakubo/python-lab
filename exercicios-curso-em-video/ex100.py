import random


def sorteia(a):
    for i in range(1, a+1):
        num = random.randint(0, 100)
        números.append(num)


def somaPar():
    soma = 0
    for v in números:
        if v % 2 == 0:
            soma += v
    print(soma)


números = []
sorteia(5)
print(números)
somaPar()

