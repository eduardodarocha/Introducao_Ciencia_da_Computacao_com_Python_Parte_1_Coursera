def num_primos(num):
    div = 1
    cont = 0
    while div <= num: 
        if num % div == 0:
            cont += 1
            div += 1
        else:
            div += 1
    if cont == 2:
        return True
    else:
        return False
    
dig = 1
while dig > 0:
    dig = int(input('Digite um número [0 para sair]: '))        
    print(f'O número {dig}',end='')
    if num_primos(dig):
        print(" é primo")
    else:
        print(" não é primo")

limite =int(input('Limite máximo: '))

n = 2
while n < limite:
    if num_primos(n):
        print(n, end=', ')
    n += 1
