valor_normal = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input('''Selecione a forma de pagamento:
[ 1 ] à vista | DINHEIRO ou CHEQUE
[ 2 ] à vista | CARTÃO
[ 3 ] à prazo | 2x no cartão
[ 4 ] à prazo | 3x ou mais no cartão
'''))
if forma_de_pagamento == 1:
    valor_pago = valor_normal - (valor_normal * 0.1)
    print(f'O valor pago à vista no dinheiro ou cheque será de: {valor_pago}.')
elif forma_de_pagamento == 2:
    valor_pago = valor_normal - (valor_normal * 0.05)
    print(f'O valor pago à vista no cartão será de: {valor_pago, [.2]}.')
elif forma_de_pagamento == 3:
    print(f'O valor pago à prazo em 2x no cartão será de: {valor_normal}.')
elif forma_de_pagamento == 4:
    valor_pago = valor_normal + (valor_normal * 0.2)
    print(f'O valor pago à prazo em 3x ou mais no cartão será de: {valor_pago}.')
else:
    print('Forma de pagamento inválida. TENTE NOVAMENTE!!!')
