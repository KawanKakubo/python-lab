ano = int(input("Digite seu ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    daq_qnts_anos = 18 - idade
    print(f"Você ainda irá se alistar no exército em {daq_qnts_anos} anos.")
elif idade == 18:
    print("Você irá se alistar no exército esse ano!")
else:
    passaram_anos = idade - 18
    print(f"Já passaram {passaram_anos} anos de se alistar!")
