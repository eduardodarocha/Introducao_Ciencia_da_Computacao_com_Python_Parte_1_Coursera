'''Escreva um programa que receba um número inteiro na entrada, 
calcule e imprima a soma dos dígitos deste número na saída'''
soma = 0
num = int(input('Digite um número inteiro: '))
while num != 0:
    alg = num % 10
    num = num // 10
    soma = soma + alg
print(soma)      
