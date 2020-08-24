'''Escreva a função vogal que recebe um único caractere como parâmetro e 
devolve True se ele for uma vogal e False se for uma consoante. '''

def vogal(x):
    if x in 'aAeEiIoOuU':
        return True
    else:
        return False
