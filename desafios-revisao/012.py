def listar_produtos(*listas):
    lista_produtos = []
    for lista in listas:
        for produto, estoque in lista:
            lista_produtos.append(produto)
    lista_produtos = set(lista_produtos)
    lista_produtos = list(lista_produtos)
    return lista_produtos


estoque_jan = [('ABACAXI', '154'), ('AAXI', '1524'), ('BACAXI', '15412')]
estoque_fev = [('AB', '154'), ('ABAC', '154'), ('ABACAXI', '154'), ('ABACI', '154')]


print(listar_produtos(estoque_fev, estoque_jan))