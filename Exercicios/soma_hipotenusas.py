def e_hipotenusa(n):
    i = 1
    j = 1
    while i < n:
        while j < n:
            if n**2 == i**2 + j**2:
                return True
            j += 1
        i += 1
        j = 1
    return False


def soma_hipotenusas(num):
    somatotal = 0
    for c in range(1, num+1):
        if e_hipotenusa(c):
            somatotal += c
    return somatotal
