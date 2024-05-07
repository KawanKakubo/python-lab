from random import randint

numero = str(randint(100000000, 999999999))
novocpf = numero
verificadores = []
acumulador = 0

for i, mult in zip(range(9), range(10, 1, -1)):
    acumulador += int(novocpf[i]) * mult

d1 = 11 - (acumulador % 11)
if d1 > 9:
    d1 = 0
verificadores.append(d1)
novocpf += str(verificadores[0])

acumulador = 0
for i, mult in zip(range(10), range(11, 1, -1)):
    acumulador += int(novocpf[i]) * mult

d2 = 11 - (acumulador % 11)
if d2 > 9:
    d2 = 0
verificadores.append(d2)
novocpf += str(verificadores[1])

print("CPF Gerado:", novocpf)
