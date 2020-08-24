'''Escreva um programa que calcula as raízes de uma equação do segundo grau.
O programa deve receber os parâmetros aa, bb, e cc da equação ax^2 + bx + c respectivamente, 
e imprimir o resultado na saída da seguinte maneira:
Quando não houver raízes reais imprima:
"esta equação não possui raízes reais"
Quando houver apenas uma raiz real imprima:
"a raiz desta equação é X"
onde X é o valor da raiz
Quando houver duas raízes reais imprima:
"as raízes da equação são X e Y"
onde X e Y são os valor das raízes.
Além disso, no caso de existirem 2 raízes reais, elas 
devem ser impressas em ordem crescente. 
Exemplos:
as raízes da equação são 1.0 e 2.0
as raízes da equação são -2.0 e 0.0   '''

import math 
a = float(input('Digite o valor de "a": '))
b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))
delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print('esta equação não possui raízes reais')
    # print('Δ < 0 -> Esta equação não possui raízes reais')
if delta == 0:
    x = -b / (2 * a)
    print('a raiz desta equação é', x)
    #  print('O valor da raiz x1 e x2 é:', x)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    #  print(f'O valor da raiz x1 é {x1} e o valor da raiz x2 é {x2}')
    if x1 < x2:
        print(f'as raízes da equação são {x1} e {x2}')
    else:
        print(f'as raízes da equação são {x2} e {x1}')