import math

def deltafunc(a, b, c):
    return (b**2) - (4 * a * c)

def calc_x1_x2(a, b, c):
    deltaval = deltafunc(a, b, c)
    if deltaval < 0:
        return print('Δ < 0 -> Esta equação não possui raízes reais')
    if deltaval == 0:
        xs = (-b - math.sqrt(deltaval)) / (2 * a)
        #saida = f'O valor da raiz x1 e x2 é: {xs:.2f}'
        return print(f'O valor da raiz x1 e x2 é: {xs:.2f}')
    if deltaval > 0:
        xp = (-b + math.sqrt(deltaval)) / (2 * a)
        xs = (-b - math.sqrt(deltaval)) / (2 * a)
        return print(f'O valor da raiz x1 é {xp:.2f} e o valor da raiz x2 é {xs:.2f}')
    else:
        return None
    
    
def main():
    vala = float(input('Digite o valor de "a": '))
    valb = float(input('Digite o valor de "b": '))
    valc = float(input('Digite o valor de "c": '))
    print(calc_x1_x2(vala, valb, valc))

main()