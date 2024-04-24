grupo = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))

    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    grupo.append(dados[:])
    dados.clear()

    continuar = str(input("Você deseja continuar (S/N)? "))
    if continuar in 'Nn':
        break

print(f'A lista dos dados foi: {grupo}.')
print(f'Foram cadastradas {len(grupo)} pessoas.')
print(f'O maior peso foi: {maior}. Peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}.', end='')
print()
print(f'O menor peso foi: {menor}. Peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}.', end='')
print()
