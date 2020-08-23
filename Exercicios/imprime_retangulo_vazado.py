lar = int(input('digite a largura: '))
alt = int(input('digite a altura: '))
contlar = 1
contalt = 1

while contalt <= alt:
    if contalt == 1 or contalt == alt:
        while contlar <= lar:
            print("#", end='')
            contlar += 1
        print()
        contlar = 1
        contalt += 1
    else:
        while contlar <= lar:
            if contlar == 1 or contlar == lar:
                print("#", end='')
                contlar += 1
            else:
                print(' ',end='')
                contlar += 1
        print()
        contlar = 1
        contalt += 1
    
    