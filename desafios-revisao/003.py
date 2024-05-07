fname = str(input('Digite seu primeiro nome: '))
if len(fname) <= 4:
    print('Seu nome é curto!')
elif len(fname) < 7:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
