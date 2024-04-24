acumulador = 0
contador = 0
for c in range(1, 7):
    n1 = int(input(f"Digite o {c}° inteiro: "))
    if n1 % 2 == 0:
        acumulador += + n1
        contador += 1
print(f'A soma entre os {contador} números pares digitados é: {acumulador}.')
