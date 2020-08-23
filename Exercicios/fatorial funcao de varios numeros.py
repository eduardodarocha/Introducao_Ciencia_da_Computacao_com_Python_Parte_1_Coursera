def fatorial(num):
    cont = 1
    fat = 1
    while cont <= num:
        fat = fat * cont
        cont += 1
    print(f'O fatorial de {num} é {fat}')
    

num = int(input('Digite um numero para fatoração [-1 para sair]: '))
while num >= 0:
    fatorial(num)
    num = int(input('Digite um numero para fatoração [-1 para sair]: '))
print('Fim')    
    
