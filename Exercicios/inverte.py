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
        