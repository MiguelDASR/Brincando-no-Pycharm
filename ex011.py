l = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
a = al * l
p = a / 2
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m²'.format(l, al, a))
print('Para pintar essa parede precisaremos de {}L de tinta.'.format(p))
