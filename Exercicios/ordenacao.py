'''Receba 3 números inteiros na entrada e imprima "crescente"
se eles forem dados em ordem crescente. Caso contrário, imprima
"não está em ordem crescente" '''

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
if num1 < num2 < num3:
    print('crescente')
else:
    print('não está em ordem crescente')
    