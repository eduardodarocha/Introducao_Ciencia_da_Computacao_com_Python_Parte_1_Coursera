'''Escreva a função remove_repetidos que recebe como parâmetro uma lista com 
números inteiros, verifica se tal lista possui elementos repetidos e os remove. 
A função deve devolver uma lista correspondente à primeira lista, sem elementos 
repetidos. A lista devolvida deve estar ordenada. '''

def remove_repetidos(lis):
    listanova = []
    for item in lis:
        if item not in listanova:
            listanova.append(item)
    return sorted(listanova)