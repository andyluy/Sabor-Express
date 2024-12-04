impares = []
maximo = int(input('Digite um valor inteiro positivo: '))

i = 1
while i < maximo:
    resto = i%2
    if resto == 1:
        impares.append(i)
    i = i + 1
print(impares)