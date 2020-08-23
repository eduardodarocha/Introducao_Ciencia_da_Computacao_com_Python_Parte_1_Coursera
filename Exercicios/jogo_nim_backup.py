def main():
    print('Bem-vindo ao jogo do NIM! Escolha:', end='\n\n')
    qtjogos = '0'
    while qtjogos != '1' or '2':
        qtjogos = input('''1 - para jogar uma partida isolada
2 - para jogar um campeonato ''')
        print()
        if qtjogos == '1':
            print('Você escolheu uma partida isolada!',end='\n\n')
            qtjogos = int(qtjogos)
            break
        if qtjogos == '2':
            print('Voce escolheu um campeonato!', end='\n\n')
            qtjogos = int(qtjogos)
            break
    campeonato(qtjogos)
    
"""Função main() - sem validação para entrada de caracters alfabéticos,
somente numericos (só vale 1 e 2) / (3, 4, 5,... não são válidos)
# def main():
#     print('Bem-vindo ao jogo do NIM! Escolha:', end='\n\n')
#     qtjogos = int(input('''1 - para jogar uma partida isolada
# 2 - para jogar um campeonato '''))
#     while qtjogos != 1 or 2:
#         if qtjogos == 1:
#             print('\nVocê escolheu uma partida isolada!',end='\n\n')
#             print('campeonato(qtjogos)1')
#             break
#         if qtjogos == 2:
#             print('\nVoce escolheu um campeonato!', end='\n\n')
#             print('campeonato(qtjogos)2')
#             break
#         qtjogos = int(input('''\n1 - para jogar uma partida isolada
# 2 - para jogar um campeonato '''))
"""
   
def usuario_escolhe_jogada(n, m):
    #pylint: disable=unused-argument
    cont = False
    while cont != True:
        retirada_user = int(input('Quantas peças você vai tirar? '))
        if retirada_user == 0 or retirada_user > m:
            print('\nOops! Jogada inválida! Tente de novo.')
            print()
        else:
            return retirada_user
        
def computador_escolhe_jogada(n, m):
    for c in range(1, m):
        if (n - c) % (m + 1) == 0:
            return c
    return m


def campeonato(jogos):
    if jogos == 1:
        print('**** Rodada 1 ****', end='\n\n')
        return print(partida(), end='\n\n')
         
    else:
        for i in range(1, 4):
            print(f'**** Rodada {i} ****', end='\n\n')
            print(partida(), end='\n\n')
    return print('''**** Final do campeonato! ****

Placar: Você 0 X 3 Computador''')    
    
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    if n % (m + 1) == 0:
        print('Voce começa!', end='\n\n')
        while n != 0:
            retirada_user = usuario_escolhe_jogada(n, m)
            if retirada_user == 1:
                print('Você tirou uma peça.')
            else:
                print(f'Você tirou {retirada_user} peças.')
            n = n - retirada_user
            if n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.', end='\n\n')
            else:
                print(f'Agora restam {n} peças no tabuleiro.', end='\n\n')
            retirada_computer = computador_escolhe_jogada(n, m)
            if retirada_computer == 1:
                print('O computador tirou uma peça.')
            else:
                print(f'O computador tirou {retirada_computer} peça.')
            n = n - retirada_computer
            if n == 0:
#                 print('Fim do jogo! O computador ganhou!')
                return 'Fim do jogo! O computador ganhou!'
            if n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.', end='\n\n')
            else:
                print(f'Agora restam {n} peças no tabuleiro.', end='\n\n')
    else:
        #if n % (m + 1) != 0:
        print('Computador começa!')
        while n != 0:
            retirada_computer = computador_escolhe_jogada(n, m)
            if retirada_computer == 1:
                print('\nO computador tirou uma peça.')
            else:
                print(f'O computador tirou {retirada_computer} peça.')
            n = n - retirada_computer
            if n == 0:
                return 'Fim do jogo! O computador ganhou!'
                
            if n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.', end='\n\n')
            else:
                print(f'Agora restam {n} peças no tabuleiro.', end='\n\n')
                
            retirada_user = usuario_escolhe_jogada(n, m)
            if retirada_user == 1:
                print('\nVocê tirou uma peça.')
            else:
                print(f'Você tirou {retirada_user} peças.')
            n = n - retirada_user
            if n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.', end='\n\n')
            else:
                print(f'Agora restam {n} peças no tabuleiro.', end='\n\n')
    

main()