numeros = list()
continuar = 'S'
while continuar in 'Ss':

    n = (int(input("Digite um número: ")))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Número duplicado, não será adicionado à lista!')

    continuar = str(input('Você deseja continuar (S/N)? '))

numeros.sort()
print(numeros)
