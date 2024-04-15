listanum = list()
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input("Digite um número: ")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print(f'Você digitou os valores: ')
print(f'O maior elemento da lista foi o {maior} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor elemento da lista foi o {menor} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
