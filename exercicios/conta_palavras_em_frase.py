def contar_palavras(frase):
    """Conta a frequência de cada palavra em uma frase.

    Args:
        frase: A frase a ser analisada.

    Returns:
        Um dicionário onde as chaves são as palavras e os valores são as frequências.
    """

    palavras = frase.split()  # Divide a frase em palavras
    contagem_palavras = {}

    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1

    return contagem_palavras

# Exemplo de uso:
frase = "Esta é uma frase de exemplo. Esta palavra se repete."
resultado = contar_palavras(frase)
print(resultado)