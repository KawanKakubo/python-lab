l1 = int(input('Digite um lado do triângulo: '))
l2 = int(input('Digite outro lado do triângulo: '))
l3 = int(input('Digite o último lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('É possível formar um triângulo!')
    if l1 == l2 == l3:
        print('Forma-se um triângulo equilátero.')
    elif l1 != l2 != l3 != l1:
        print('Forma-se um triângulo escaleno')
    else:
        print('Forma-se um triângulo isósceles.')
else:
    print('Não é possível formar um triângulo!')
