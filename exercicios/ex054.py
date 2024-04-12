from datetime import date
atual_ano = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    ano_de_nascimento = int(input(f'Qual o ano de nascimento da {pessoa}° pessoa? '))
    idade = (atual_ano - ano_de_nascimento)
    if idade >= 18:
        totmaior += + 1
    else:
        totmenor += + 1
print(f"{totmaior} pessoas tem acima de 18 anos e {totmenor} ainda estão na menoridade.")
