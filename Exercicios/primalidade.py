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
        
