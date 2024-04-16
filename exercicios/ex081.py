listanum = []
continuar = 'S'

while continuar in 'Ss':
    n = int(input("Digite um número: "))
    listanum.append(n)
    continuar = str(input("Deseja continuar (S/N)? "))

print(f'Foram digitados {len(listanum)} números.')
listanum.sort(reverse=True)
print(f'A lista de valores ordenada de forma decrescente é: {listanum}')
if 5 in listanum:
    print(f'O número 5 se encontra na lista!')
else:
    print(f'O número 5 não se encontra na lista!')
