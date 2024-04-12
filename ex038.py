a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
if a > b:
    print(f"O primeiro valor digitado, {a}, é maior que, {b}.")
elif a < b:
    print(f"O segundo valor digitado, {b}, é maior que o primeiro, {a}.")
else:
    print("Ambos os valores digitados possuem o mesmo valor.")
