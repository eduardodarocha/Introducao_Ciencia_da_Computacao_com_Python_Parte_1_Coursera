def fatorial(x):
    '''
    Calcula o fatorial de x
    '''
    if x < 0:
        return 0
    fat = 1
    for i in range(1, x+1):
        fat = fat * i  
    return fat

def test_fatorial0():
    assert  fatorial(0) == 1
    
def test_fatorial1():
    assert  fatorial(1) == 1
    
def test_fatorial_negativo():
    assert  fatorial(-10) == 0

def test_fatorial4():
    assert  fatorial(4) == 24

def test_fatorial5():
    assert  fatorial(5) == 120