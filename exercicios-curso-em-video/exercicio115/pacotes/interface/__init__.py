colors = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'blue': '\033[34m',
    'green': '\033[32m',
    'yellow': '\033[33m'
}

cor = colors['reset']


def linha(tam=42):
    return '-' * tam


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(colors['red'], 'ERRO: por favor, digite um número inteiro válido!', colors['reset'])
            continue
        except KeyboardInterrupt:
            print(colors['red'], '\nEntrada de dados interrompida pelo usuário!', colors['reset'])
            return 0
        else:
            return n


def cabeçalho(txt):
    print(colors['green'], linha(), colors['reset'])
    print(colors['blue'], txt.center(42), colors['reset'])
    print(colors['green'], linha(), colors['reset'])


def menu(lista):
    c = 1
    for i in lista:
        print(colors['yellow'], f'{c} - {i}', colors['reset'])
        c += 1
    print(colors['green'], linha(), colors['reset'])
    opc = leiaInt('Sua Opção: ')
    return opc
