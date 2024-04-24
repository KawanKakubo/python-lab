n1 = float(input("Digite o valor da sua primeira nota: "))
n2 = float(input("Digite o valor da sua segunda nota: "))
m = ( n1 + n2 ) / 2
if m < 5:
    print(f"Sua média foi de {m}. Você está reprovado, que pena!")
elif 5 < m < 6.9:
    print(f"Sua média foi de {m}. Você está de recupeção, ainda é possível passar de ano!")
else:
    print(f"Sua média foi de {m}. Você está aprovado!")
