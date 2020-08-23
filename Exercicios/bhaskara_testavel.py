import math
class Bhaskara:

    def deltafunc(self, a, b, c):
        return (b**2) - (4 * a * c)

    def calc_x1_x2(self, a, b, c):
        deltaval = self.deltafunc(a, b, c)
        if deltaval < 0:
            return 0 #print('Δ < 0 -> Esta equação não possui raízes reais')
        if deltaval == 0:
            xs = (-b - math.sqrt(deltaval)) / (2 * a)
            #saida = f'O valor da raiz x1 e x2 é: {xs:.2f}'
            return 1, xs #print(f'O valor da raiz x1 e x2 é: {xs:.2f}')
        if deltaval > 0:
            xp = (-b + math.sqrt(deltaval)) / (2 * a)
            xs = (-b - math.sqrt(deltaval)) / (2 * a)
            return xp, xs  #print(f'O valor da raiz x1 é {xp:.2f} e o valor da raiz x2 é {xs:.2f}')
        else:
            return None
b = Bhaskara()    
print(b.calc_x1_x2(-10, 20, 10))
