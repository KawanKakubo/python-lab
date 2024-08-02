def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def falaOi(nome):
    return f'Oi, {nome}'


def saudacao(nome, frase):
    return f'{frase}, {nome}'


exe = mestre(falaOi, 'Kawan')
print(exe)
