menorp = 0
maiorp = 0
for pessoas in range (1, 6):
    peso = float(input(f'Digite o peso da {pessoas}° pessoa: '))
    if pessoas == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f"O maior peso das pessoas mencionadas foi: {maiorp}.")
print(f"O menor peso das pessoas mencionadas foi: {menorp}.")
