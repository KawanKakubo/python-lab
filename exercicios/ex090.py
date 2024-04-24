dicionario = dict()
dicionario['Nome'] = str(input("Digite seu nome: "))
dicionario['Média'] = float(input("Digite sua média: "))

if dicionario['Média'] >= 6:
    dicionario['Situacao'] = 'Aprovado'
else:
    dicionario['Situacao'] = 'Reprovado'

for k, v in dicionario.items():
    print(f'{k} é {v}.')
