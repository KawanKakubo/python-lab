l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
l3 = [v * 2 for v in l1]
l4 = [(v, v2) for v in l1 for v2 in range(3)]
l1b = ['Luiz', 'Mauro', 'Maria']
l5 = [v.replace('a', '@').upper() for v in l1b]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex = [(y, x) for x, y in tupla]
ex = dict(ex)

lex = list(range(100))
ex2 = [v for v in lex if v % 3 == 0 if v % 8 == 0]

ex3 = [v if v % 3 == 0 else 'n é' for v in lex]

print(ex3)