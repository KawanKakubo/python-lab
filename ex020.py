import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
l = [a1, a2, a3, a4]
s = random.shuffle(l)
print(f'A ordem de apresentação dos trabalhos será: ')
print(l)
