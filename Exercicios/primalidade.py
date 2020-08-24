'''Escreva um programa que receba um número inteiro positivo na entrada 
e verifique se é primo. Se o número for primo, imprima "primo". 
Caso contrário, imprima "não primo".  '''

num = int(input('Digite um número inteiro: '))
cont = num
primo = 0
while cont > 0:
    if num % cont == 0:
        primo = primo + 1
        cont -= 1
    else:     
        cont -= 1
if primo == 2:
    print('primo')
else:
    print('não primo')
        
