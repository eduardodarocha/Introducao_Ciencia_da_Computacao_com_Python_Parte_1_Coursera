'''Escreva a função soma_elementos que recebe como parâmetro uma 
lista com números inteiros e devolve um número inteiro 
correspondente à soma dos elementos da lista recebida. '''

def soma_elementos(lis):
    total = 0
    for item in lis:
        total = total + item
    return total