valor_da_casa = float(input('Digite o valor da casa: '))
salario_do_comprador = float(input('Digite o salário do comprador: '))
anos = float(input('Digite em quantos anos o comprador irá pagar pela casa: '))
prestacao = valor_da_casa / anos
if prestacao >= 0.3 * salario_do_comprador:
    print('Seu empréstimo foi negado, que pena!')
else:
    print('Parabéns, seu empréstimo foi aceito!')
