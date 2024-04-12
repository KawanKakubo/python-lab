
idadetotal = 0
maioridadehomem = 0
nomevelho = ''
qntmulher = 0

for pessoas in range(1, 5):
    print(f'----- {pessoas}° Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [m/f]: ')).strip()

    idadetotal += idade

    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        qntmulher += 1

media = idadetotal / 4

print("=" * 21)
print(f'A média entre as idades de todas as pessoas foi: {media}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'No cadastro acima, {qntmulher} pessoas são mulheres menores que 20 anos.')
