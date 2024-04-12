ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2024 - ano_nascimento
if idade <= 9:
    print(f"Você possui {idade} anos e se encontra na categoria MIRIM.")
elif 9 < idade <= 14:
    print(f"Você possui {idade} anos e se encontra na categoria INFANTIL.")
elif 14 < idade <= 19:
    print(f"Você possui {idade} anos e se encontra na categoria JUNIOR.")
else:
    print(f"Você possui {idade} anos e se encontra na categoria MASTER.")
