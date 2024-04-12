pessoas = 1
idadesoma = 0
homemqnt = 0
mulhermenos20 = 0

while True:
    idade = (int(input(f"Digite a idade da {pessoas}° pessoa: ")))
    sexo = ' '
    while sexo not in 'MF':
        sexo = (str(input(f"Digite o sexo da {pessoas}° pessoa [M|F]: "))).strip().upper()[0]

    if idade >= 18:
        idadesoma += 1
    if sexo == 'M':
        homemqnt += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1

    pessoas += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Você deseja continuar [S|N]? ")).strip().upper()[0]
    if continuar == 'N':
        break


print(f'{idadesoma} pessoas tem mais de 18 anos.')
print(f'{homemqnt} homens foram cadastrados.')
print(f'{mulhermenos20} mulheres tem menos de 20 anos.')