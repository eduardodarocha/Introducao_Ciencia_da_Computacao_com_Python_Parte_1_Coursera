def maximo(x, y, z):
    maior = x
    if y >= maior:
        maior = y
    if z >= maior:
        maior = z
    return maior
