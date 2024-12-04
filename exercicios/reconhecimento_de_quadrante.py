x = float(input('Digite a coordenada X: '))
y = float(input('Digite a coordenada Y: '))

if x > 0:
    if y >= 0:
        print('Você está no primeiro quadrante')
    if y < 0:
        print('Você está no quarto quadrante')
else :
    if y >= 0:
        print('Você está no segundo quadrante')
    if y < 0:
        print('Você está no terceiro quadrante')