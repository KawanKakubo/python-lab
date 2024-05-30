perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual a raiz quadrada de 144?',
        'resposta': {
            'a': '10',
            'b': '12',
            'c': '11',
            'd': '9',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual a raiz quadrada de 121?',
        'resposta': {
            'a': '10',
            'b': '12',
            'c': '11',
            'd': '9',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Qual a raiz quadrada de 100?',
        'resposta': {
            'a': '10',
            'b': '12',
            'c': '11',
            'd': '9',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Qual a raiz quadrada de 81?',
        'resposta': {
            'a': '10',
            'b': '12',
            'c': '11',
            'd': '9',
        },
        'resposta_certa': 'd',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv["resposta"].items():
        print(f'{rk}) {rv}')
    for respostacerta in pv["resposta_certa"]:
        resp = input('Resposta: ')
        if resp == respostacerta:
            print('ACERTOU!')
            respostas_certas += 1
        else:
            print('ERROU!')

qtd_perguntas = len(perguntas)
pcrt_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas!')
print(f'Sua porcentagem de acertos foi de: {pcrt_acerto:.2f}%')