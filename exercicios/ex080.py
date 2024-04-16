numeros = list()

for c in range(0,5):
    n = int(input("Digite um valor numérico: "))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1

print(numeros)
