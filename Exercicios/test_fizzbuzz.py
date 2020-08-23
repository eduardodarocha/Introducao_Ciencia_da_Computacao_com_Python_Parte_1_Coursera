def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 != 0):
        return "Fizz"
    elif (x % 3 != 0) and (x % 5 ==0): 
        return "Buzz"
    elif (x % 3 == 0) and (x % 5 ==0):
        return '"FizzBuzz"'
    else:
        return x

def test_answer3():
    assert fizzbuzz(3) == "Fizz"
    
def test_answer5():
    assert fizzbuzz(5) == "Buzz"
    
def test_answer15():
    assert fizzbuzz(15) == "FizzBuzz"

def test_answerx():
    assert fizzbuzz(4) == 4
