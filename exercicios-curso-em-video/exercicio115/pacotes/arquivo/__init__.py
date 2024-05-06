colors = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'blue': '\033[34m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'white': '\033[37m'
}


def arquivoExiste(nome):
    try:
        arquivo = open(nome, "rt")
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print(colors['red'], 'Houve um erro na criação do arquivo.', colors['reset'])
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        arquivo = open('pessoas-cadastradas.txt', 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for linha in arquivo:
            dado = linha.split('-')
            dado[1] = dado[1].replace('\n', '')
            print(colors['white'], f'{dado[0]:<30}{dado[1]:>7} anos', colors['reset'])
    finally:
        arquivo.close()


def escreverArquivo(arq, name='desconhecido', age=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        # Escrever dados no arquivo
        try:
            arquivo.write(f'{name}-{age}\n')
        except:
            print('Erro ao escrever os dados.')
        else:
            print(colors['green'], f'Registro de {name} realizado com sucesso.', colors['reset'])
    finally:
        arquivo.close()