def metade(n, f=False):
    if f is True:
        return moeda(n/2)
    else:
        return n/2


def dobro(n, f=False):
    if f is True:
        return moeda(n*2)
    else:
        return n * 2


def aumentar(n, p, f=False):
    if f is True:
        return moeda(n + (p/100 * n))
    else:
        return n + (p/100 * n)


def diminuir(n, p, f=False):
    if f is True:
        return moeda(n - (p / 100 * n))
    else:
        return n - (p / 100 * n)


def moeda(v=0, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')


def resumo(v=0, a=10, r=5):
    print('-' * 40)
    print(f'{'Resumo do Valor'.center(40)}')
    print('-' * 40)
    print(f'Preço analisado: \t\t\t\t{moeda(v)}')
    print(f'Dobro do preço: \t\t\t\t{dobro(v, f=True)}')
    print(f'Metade do preço: \t\t\t\t{metade(v, f=True)}')
    print(f'Acréscimo de {a} do preço: \t\t{aumentar(v, a, f=True)}')
    print(f'Redução de {r} do preço: \t\t{diminuir(v, r, f=True)}')