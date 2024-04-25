info_pessoais = dict()
info_pessoais['Nome'] = str(input("Nome: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
info_pessoais['Idade'] = 2024 - ano_nascimento
info_pessoais['CTPS'] = int(input("Digite sua carteira de trabalho (0 não tem): "))

if info_pessoais['CTPS'] != 0:
    info_pessoais['Ano de Contratação'] = int(input("Digite seu ano de contratação: "))
    info_pessoais['Salário'] = float(input("Digite seu salário: "))
    ano_aposentadoria = 30 + info_pessoais['Ano de Contratação']
    info_pessoais['Idade Aposentadoria'] = ano_aposentadoria - ano_nascimento

for k, v in info_pessoais.items():
    print(f'{k} tem o valor {v}.')
