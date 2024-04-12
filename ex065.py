n = int(input("Digite um número inteiro: "))

acumulador = contador = 0
maior = menor = None
continuar = 'S'

while continuar in 'Ss':

    contador += 1
    acumulador += n

    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    continuar = str(input("Você deseja continuar [S|N]? "))
    if continuar in 'Ss':
        n = int(input('Digite novamente outro número inteiro : '))
    elif continuar in 'Nn':
        print('Saindo do programa.')

print('Você finalizou o programa!')
media = acumulador / contador
print(f"A média entre os valores digitados é: {media:.2f}")
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
