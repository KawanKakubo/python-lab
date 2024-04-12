palavras = ('FUTURO', 'CARRO', 'BEISEBOL', 'LIXO', 'UTFPR', 'ASSAI')
for elementos in palavras:
    print(f'\nNa palavra {elementos}, temos as vogais: ', end='')
    for letras in elementos:
        if letras in 'AEIOU':
            print(letras, end=' ')
