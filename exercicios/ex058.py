import random

l = [0,1,2,3,4,5,6,7,8,9,10]
num = random.choice(l)
acumulador = 1
usernum = int(input('Digite um número inteiro de 0 à 10: '))

while usernum != num:
    usernum = int(input('Número errado! Digite novamente um número inteiro de 0 à 10: '))
    acumulador += 1

print(f"Parabéns você acertou o número escolhido pelo computador, que foi o {num}! Foram necessários {acumulador} tentativas!")