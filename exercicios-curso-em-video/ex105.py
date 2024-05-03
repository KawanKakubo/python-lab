def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não aceitar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    acumulador = cont = maior = menor = 0
    dicionario = {}

    for i, v in enumerate(num):
        cont += 1
        acumulador += v
        if i == 0:
            maior = menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v

    media = acumulador / cont

    dicionario["total"] = cont
    dicionario["maior"] = maior
    dicionario["menor"] = menor
    dicionario["media"] = media

    if sit == True:

        if media > 7:
            situacao = 'BOM'
        if media < 7:
            situacao = 'RAZOAVEL'
        if media < 6:
            situacao = 'RUIM'

        dicionario["sit"] = situacao

    print(dicionario)

resp = notas(10, 8, 7, sit=True)
help(notas)
