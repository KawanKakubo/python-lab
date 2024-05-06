from pacotes.interface import *
from pacotes.arquivo import *
from time import sleep

colors = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'blue': '\033[34m',
    'green': '\033[32m'
}

arq = 'pessoas-cadastradas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('SISTEMA ARQUIVO 1.0')
while True:
    cor = colors['reset']
    r = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if r == 1:
        sleep(0.5)  # Ler todo o conteúdo de um arquivo
        cabeçalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
        sleep(0.5)
        cabeçalho('SISTEMA ARQUIVO 1.0')

    elif r == 2:
        sleep(0.5)
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        escreverArquivo(arq, nome, idade)
        sleep(0.5)
        cabeçalho('SISTEMA ARQUIVO 1.0')

    elif r == 3:
        sleep(0.5)
        cabeçalho('SAINDO DO SISTEMA')
        break

    else:
        sleep(0.5)
        print(colors['red'], 'ERRO! Digite uma opção válida!', colors['reset'])
