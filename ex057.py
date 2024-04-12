sexo = str(input('Digite seu sexo [M|F]: ')).upper().strip()[0]
while sexo not in 'MF':
    print('Digite seu sexo novamente, aparentemente houve um erro!')
    sexo = str(input("Digite seu sexo [M|F]: ")).upper().strip()[0]
print(f"Sexo {sexo} validado com sucesso!")
