n = int(input("Digite um número inteiro [999 para parar]: "))
acumulador = 0
contador = 1
while n != 999:
    contador += 1
    acumulador += n
    n = int(input('Digite novamente outro número inteiro [999 para parar]: '))
print('Você finalizou o programa!')
print(f'Para isso foram necessárias {contador} tentativas e a soma entre todos os números digitados foram: {acumulador}.')