def main():
    cont = 0
    n = int(input('Digite n: '))
    lista = list()
    while cont < n:
        item = int(input('Digite um número da sequência: '))
        lista.append(item)
        cont += 1
    cont2 = -1
    for i in lista:
        print(lista[cont2], end=' ')
        cont2 += -1

                   
main()

# lista = []
# while True:
#     num = int(input('Digite um número [0 para sair]: '))
#     if num != 0:
#         lista.append(num)
#         print(lista)
#     else:
#         lista.reverse()
#         print(lista)
#         break