def ex3(texto):
    if len(texto) == 0:
        return texto
    return texto[-1] + ex3(texto[:-1])

ex3()