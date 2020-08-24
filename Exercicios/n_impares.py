'''Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
Digite o valor de n: 5
1
3
5
7
9
'''

quant = int(input('Digite o valor de n: '))
cont = 0
num = 1
while quant > cont:
    print(num)
    num += 2
    quant -= 1
