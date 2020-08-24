'''Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 
como parâmetro e devolve o maior número primo menor ou igual ao número passado à função'''

def maior_primo(x):
    for cont in range(2, x+1):
        if primo(cont) == True:
            maior = cont
    return maior
    
def primo(k):
    contprimo = 1
    for cont in range(1, k):
        if k % cont == 0:
            contprimo += 1
    if contprimo == 2:
        return True
    else:
        return False
