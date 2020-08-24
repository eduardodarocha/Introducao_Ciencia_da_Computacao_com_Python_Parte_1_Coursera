'''Escreva um programa que recebe como entradas (utilize a função input) 
dois números inteiros correspondentes à largura e à altura de um retângulo, 
respectivamente. O programa deve imprimir uma cadeia de caracteres que 
represente o retângulo informado com caracteres '#' na saída.'''

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
