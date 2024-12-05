quadrados = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
print(quadrados)

# Utilizando loop
quadrados = {}
for numero in range(1, 6):
    quadrados[numero] = numero ** 2

print(quadrados)