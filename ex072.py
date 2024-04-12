numex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input("Digite um número entre 0 e 20: "))
while 0 > num or 20 < num:
    num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f'Você digitou o número {numex[num]}.')
