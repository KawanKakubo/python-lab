numeros = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
           int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
cont = 0

print(f'Você digitou os valores {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vez.')
print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição.')

for elementos in numeros:
    if elementos % 2 == 0:
        cont += 1

print(f'Houve {cont} valores pares digitados.')
