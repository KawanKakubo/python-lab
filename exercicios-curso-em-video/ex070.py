produto = 1
totpreco = maisde1000 = menor = preco = cont = 0

while True:
    produtonome = str(input(f"Digite o nome do {produto}° produto: ")).strip().title()
    preco = int(input(f"Digite o preço do {produtonome}: "))
    totpreco += preco
    cont += 1
    if preco > 1000:
        maisde1000 += 1
    if cont == 1:
        menor = preco
        produtobarato = produtonome
    else:
        if preco < menor:
            menor = preco
            produtobarato = produtonome
    produto += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Você deseja continuar [S|N]? ")).strip().upper()[0]
    if continuar == 'N':
        break


print(f'R${totpreco:.2f} foi o total gasto na compra.')
print(f'{maisde1000} produtos ultrapassaram o valor de R$1000.00')
print(f'{produtobarato} é o produto mais barato, custando apenas R${menor:.2f}')