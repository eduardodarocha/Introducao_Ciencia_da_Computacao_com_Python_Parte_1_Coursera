'''Instruções sobre esse exercico estão em no arquivo anexo: 
"instrucao_exercico_Similaridades_entre_textos-Caso_COH-PIAH.md" '''

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e
    devolve uma assinatura a ser comparada com os textos fornecidos'''
    
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma
    lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print()

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma
    lista das sentencas dentro do texto (sentenças entre -> . ! ? )'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma
    lista das frases dentro da sentenca (frases entre -> , : ;)'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma
    lista das palavras dentro da frase (palavras entre -> espaços)'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve
    o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve
    o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto
    e deve devolver o grau de similaridade nas assinaturas.'''
    sabaux = 0
    for i, v1 in enumerate(as_a):
        for j, v2 in enumerate(as_b):
            if i == j:
                sabaux = abs(v1 - v2) + sabaux     
    return sabaux / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve
    devolver a assinatura do texto.'''
#---------------------------------------------------------------------
# Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    tampal = 0
    tam = 0
    totcarac = 0
    totsen = totcaracfra = 0
    totfra = 0
    totpal = []
    senmedia = separa_sentencas(texto)
    for s in senmedia:
        framedia = separa_frases(s)
        totsen = totsen + 1
        for cf in framedia:
            totcaracfra = totcaracfra + len(cf)
        for c in s:
            totcarac = totcarac + len(c)
        for f in framedia:
            palmedia = separa_palavras(f)
            totfra = totfra + 1
            for p in palmedia:
                tampal = len(p) + tampal
                tam = tam + 1
                totpal.append(p)

    wal = tampal / tam

#---------------------------------------------------------------------
# Relação Type-Token: Número de palavras diferentes utilizadas
# em um texto divididas pelo total de palavras.
    ttr = n_palavras_diferentes(totpal) / tam
    
#---------------------------------------------------------------------
# Razão Hapax Legomana: Número de palavras utilizadas
# uma única vez dividido pelo número total de palavras.
    hlr = n_palavras_unicas(totpal) / tam

#---------------------------------------------------------------------
# Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    tampal = 0
    tam = 0
    totcarac = 0
    totsen = totcaracfra = 0
    totfra = 0
    totpal = []
    senmedia = separa_sentencas(texto)
    for s in senmedia:
        framedia = separa_frases(s)
        totsen = totsen + 1
        for cf in framedia:
            totcaracfra = totcaracfra + len(cf)
        for c in s:
            totcarac = totcarac + len(c)
        for f in framedia:
            palmedia = separa_palavras(f)
            totfra = totfra + 1
            for p in palmedia:
                tampal = len(p) + tampal
                tam = tam + 1
                totpal.append(p)

    wal = tampal / tam

#---------------------------------------------------------------------
# Relação Type-Token: Número de palavras diferentes utilizadas
# em um texto divididas pelo total de palavras.
    ttr = n_palavras_diferentes(totpal) / tam
    
#---------------------------------------------------------------------
# Razão Hapax Legomana: Número de palavras utilizadas
# uma única vez dividido pelo número total de palavras.
    hlr = n_palavras_unicas(totpal) / tam

#---------------------------------------------------------------------
# Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    sal = totcarac / totsen
    
#---------------------------------------------------------------------
# Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    sac = totfra / totsen
    
#---------------------------------------------------------------------
# Tamanho médio de frase é a soma do número de caracteres em cada frase
# dividida pelo número de frases no texto (os caracteres que separam uma
# frase da outra não devem ser contabilizados como parte da frase).
    pal =  totcaracfra / totfra
    
#---------------------------------------------------------------------
       
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma
    assinatura ass_cp e deve devolver o numero (1 a n) do texto
    com maior probabilidade de ter sido infectado por COH-PIAH.'''
    cont = 1
    num_menor = 0
    menorsab = 0
    for t in textos:
        textoaux = calcula_assinatura(t)
        sabaux = compara_assinatura(textoaux, ass_cp)
        if cont == 1:
            menorsab = sabaux
            num_menor = cont
            cont += 1
        else:
            if sabaux < menorsab:
                menorsab = sabaux
                num_menor = cont
                cont += 1      
            
    return num_menor
    
def main():
    ass_princ = le_assinatura()
    todos_textos = le_textos()
    textocopia = avalia_textos(todos_textos, ass_princ)
    print(f'O autor do texto {textocopia} está infectado com COH-PIAH')
    
main()


