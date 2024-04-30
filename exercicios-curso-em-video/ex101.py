def voto(ano_nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nasc
    if idade < 16:
        return f'Com {idade} anos, seu voto é: NEGADO.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos, seu voto é: OPCIONAL.'
    else:
        return f'Com {idade} anos, seu voto é: OBRIGATÓRIO.'


nasc = int(input("Em qual ano você nasceu? "))
print(voto(nasc))
