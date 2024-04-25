galera = list()
pessoa = dict()
soma_idades = m = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: "))
        if pessoa['sexo'] in 'MmFf':
            break
        print('Valor incorreto, verifique a grafia novamente.')
    pessoa['idade'] = int(input("Idade: "))
    soma_idades += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Você quer continuar [S/N]: "))
        if resp in 'SsNn':
            break
        print('ERRO, verifique a grafia novamente.')
    if resp in 'Nn':
        break
print('=====')
m = soma_idades / len(galera)
print(f'{len(galera)} pessoas foram cadastradas.')
print(f'A média de idade das pessoas cadastradas foi: {m:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('As pessoas que estão acima da média de idade são: ', end='')
for p in galera:
    if p['idade'] > m:
        print(f'{p["nome"]} ', end='')