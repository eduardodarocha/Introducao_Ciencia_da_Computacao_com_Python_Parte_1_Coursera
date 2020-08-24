'''Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo 
retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, 
nn é uma hipotenusa se existem números inteiros i e j tais que:
n^2 = i^2 + j^2n 

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n 
e devolva a soma de todos os inteiros entre 1 e nn que são comprimento da hipotenusa de 
algum triângulo retângulo com catetos inteiros.

Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser 
somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 
até nn testando se o número é hipotenusa de algum triângulo e somando em caso 
afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo 
triângulos e somando as hipotenusas inteiras encontradas.
Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o 
comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não. '''

def e_hipotenusa(n):
    i = 1
    j = 1
    while i < n:
        while j < n:
            if n**2 == i**2 + j**2:
                return True
            j += 1
        i += 1
        j = 1
    return False


def soma_hipotenusas(num):
    somatotal = 0
    for c in range(1, num+1):
        if e_hipotenusa(c):
            somatotal += c
    return somatotal
