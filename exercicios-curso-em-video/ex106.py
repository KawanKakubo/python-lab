c = {
    'RESET': '\033[0m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'BLUE': '\033[34m',
}


def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{cmd}\'.', cor='BLUE')
    help(cmd)


def titulo(msg, cor='RESET'):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c['RESET'], end='')


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 'RED')
    comando = str(input("Função ou Biblioteca > "))
    if comando.lower() == 'end':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 'RED')