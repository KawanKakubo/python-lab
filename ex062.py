a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
termos = a1
cont = 1
total = 0
mais = 10

print('Os 10 primeiros termos dessa PA: ')
print(f'{a1}; ', end='')
while mais != 0:
    total += mais
    while cont < total:
        termos += r
        cont += 1
        print(f'{termos}; ', end='')
    print(' ...')
    mais = int(input("Você deseja mostrar mais quantos termos? "))
print(f'Foram exibidos {total} termos.')
print('FIM')
