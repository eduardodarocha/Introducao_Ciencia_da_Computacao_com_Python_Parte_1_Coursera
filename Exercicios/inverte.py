'''Como pedido na primeira video-aula desta semana, escreva um 
programa que recebe uma sequência de números inteiros e imprima 
todos os valores em ordem inversa. A sequência sempre termina pelo 
número 0. Note que 0 (ZERO) não deve fazer parte da sequência.'''

num = ''
lista = list()
cont = 0
while num !=0:
    num = int(input('Digite um número: '))
    if num != 0:
        lista.append(num)
for c in range(len(lista)):
    cont -= 1
    print(lista[cont])
        