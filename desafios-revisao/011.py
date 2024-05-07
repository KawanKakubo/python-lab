def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Olá, {nome}!'


def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'


exe = mestre(saudacao, 'Olá', 'Jorge')
print(exe)