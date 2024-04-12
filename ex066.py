cont = acumulador = 0
while True:
    n = int(input("Digite um número inteiro [999 para finalizar]: "))
    if n == 999:
        print('Finalizando o programa.')
        break
    cont += 1
    acumulador += n
print(f'A soma de {cont} valores é de {acumulador}.')
