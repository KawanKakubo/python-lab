l = int(input('Digite a largura da parede: '))
a = int(input('Digite a altura da parede: '))
area = l * a
volume = area / 2
print(f'A área total de sua parede são {area} metros quadrados.')
print(f'Se considerarmos que 1L de tinta pinta 2 metros quadrados, serão necessários, {volume}L de tinta.')
