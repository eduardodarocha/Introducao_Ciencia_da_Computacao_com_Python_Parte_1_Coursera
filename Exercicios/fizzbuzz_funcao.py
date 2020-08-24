'''Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
'Fizz' se o número for divisível por 3 e não for divisível por 5;
'Buzz' se o número for divisível por 5 e não for divisível por 3;
'FizzBuzz' se o número for divisível por 3 e por 5;
Caso o número não seja divisível 3 e também não seja divisível por 5, 
ela deve devolver o número recebido como parâmetro.'''

def fizzbuzz(x):
    '''Teste de docstring'''
    if (x % 3 == 0) and (x % 5 != 0):
        return "Fizz"
    elif (x % 3 != 0) and (x % 5 ==0): 
        return "Buzz"
    elif (x % 3 == 0) and (x % 5 ==0):
        return "FizzBuzz"
    else:
        return x
                 
fizzbuzz.__doc__
