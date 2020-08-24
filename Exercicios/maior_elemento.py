'''Escreva a função maior_elemento que recebe como parâmetro 
uma lista com números inteirose devolve um número inteiro 
correspondente ao maior valor presente na lista recebida. '''

def maior_elemento(lis):
    maior = lis[0]
    for item in lis:
        if item > maior:
            maior = item
    return maior   
    
            
def menor_elemento(lis):
    menor = lis[0]
    for item in lis:
        if item < menor:
            menor = item
    return menor
           
def maior_e_menor(lis):
    mai = maior_elemento(lis)
    men = menor_elemento(lis)
    print(f'Maior temperatura foi: {mai} e menor foi {men}')
    

lista_temp = [33.4, 30.2, 41.9, 34, 28.6, 29.1, 26.2, 35.4, 30.7, 32.2, 37.5, -26.4, 39.7, 29.4]
lista1 = [0]

#maior_e_menor(lista1)

def testefunctemp(listateste, valor_esperado):
    valor_calculado = menor_elemento(listateste)
    if valor_calculado != valor_esperado:
        print(f'Erro na lista: {listateste}')
        print(f'Valor calculado: {valor_calculado}. Valor esperado: {valor_esperado}')
        
        
def testa_minimo():
    print('Iniciando testes')
    testefunctemp([0], 0)
    testefunctemp([0, 0, 0, 0, 0, 0, 0, 0], 0)
    testefunctemp([0, 1, 2, 3, 4, 5, 6, 7], 0)
    testefunctemp([33.4, 30.2, 41.9, 34, 28.6, 29.1, 26.2, 35.4, 30.7, 32.2, 37.5, 26.4, 39.7, 29.4], 26.2)
    testefunctemp([-15, -10, 0, 10, 15], -15)
    print('Terminando testes')
    
testa_minimo()
# def maior_e_menor(lis):
#     maior = lis[0]
#     menor = lis[0]
#     for item in lis:
#         if item > maior:
#             maior = item
#         if item < menor:
#             menor = item
#     print(f'Maior temperatura foi: {maior}°C e menor foi {menor}°C')