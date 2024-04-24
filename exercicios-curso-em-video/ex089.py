ficha = []

while True:
    nome = (str(input("Nome: ")))
    nota1 = (float(input("Nota 1: ")))
    nota2 = (float(input("Nota 2: ")))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input("Deseja continuar (S/N): "))

    if continuar in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 26)

for i, v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:<8.2f}')
print('-=' * 30)

while True:
    opc = int(input("Mostrar notas de qual aluno (999 para sair): "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}.')
    else:
        print('Opção incorreta, digite novamente!')

print('Até mais!')
