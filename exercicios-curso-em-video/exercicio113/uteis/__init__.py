def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário!')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido!')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário!')
        else:
            return n