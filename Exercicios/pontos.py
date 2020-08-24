'''Distância entre dois pontos - Faça um programa que receba 4 números na entrada,
 um de cada vez. Os dois primeiros devem corresponder, respectivamente, às 
 coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos  devem 
 corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima "longe"
na saída. Caso o contrário, quando a distância for menor que 10, imprima "perto" '''

import math
x1 = float(input('Digite o valor de x1: '))
y1 = float(input('Digete o valor de y1: '))
x2 = float(input('Digite o valor de x2: '))
y2 = float(input('Digite o valor de y2: '))
dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
if dist >= 10:
    print('longe')
else:
    print('perto')