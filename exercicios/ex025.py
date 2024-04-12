nome = str(input('Digite seu nome: '))
n0 = nome.upper()
n1 = n0.strip().split()
print(f'Seu nome tem Silva? {'SILVA' in n1}')
