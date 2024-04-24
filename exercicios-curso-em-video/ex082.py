listanum = []
listapar = []
listaimpar = []
continuar = 'S'

while continuar in 'Ss':
    n = int(input("Digite um número: "))
    listanum.append(n)

    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

    continuar = str(input("Deseja continuar (S/N)? "))

print(f'Lista geral: {listanum}')
print(f'Lista pares: {listapar}')
print(f'Lista ímpares: {listaimpar}')
