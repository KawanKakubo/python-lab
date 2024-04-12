import math
ang = float(input('Digite um ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O ângulo {ang}° possui valor de seno: {sen:.2f}, cosseno: {cos:.2f}, tangente: {tan:.2f}.')
