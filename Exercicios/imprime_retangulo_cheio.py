lar = int(input('digite a largura: '))
alt = int(input('digite a altura: '))
contlar = contalt = 0
while contalt < alt:
    while contlar < lar:
        print("#", end='')
        contlar += 1
    print()
    contlar = 0
    contalt += 1
