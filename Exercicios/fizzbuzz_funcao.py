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
