def n_primos(n):
    cont = total = 0
    div = 1
    contotal = n
    while contotal >= 2:
        cont = 0
        while div <= n:
            if n % div == 0:
                cont += 1
                div += 1
            else:
                div += 1
        if cont == 2:
            total += 1
        contotal -= 1
        div = 1
        n -= 1
    return total
print(n_primos(6))