'''Escreva um programa que receba um número natural n na entrada 
e imprima n! (fatorial) na saída.'''
fat = 1
num = int(input('Digite o valor de n: '))
cont = num -1
while cont >= 1:
    num = num * cont
    cont -= 1
    fat = num    
print(fat)

