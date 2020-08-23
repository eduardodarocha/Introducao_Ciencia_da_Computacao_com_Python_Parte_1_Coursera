def fatorial(x):
    '''
    Calcula o fatorial de x
    '''
    fat = 1
    for i in range(1, x+1):
        fat = fat * i  
    return fat

def coef_binomial(n,k):
    '''
    Calcula o coeficiente binomial
    de n elementos com
    classe k(número de combinações)
    '''    
    cb = fatorial(n) / (fatorial(k) * (fatorial(n - k)))
    return cb
print('Coeficiente Binomial (n - elementos & k - classe)') 
n1 = int(input('Digite o números de elementos(n): '))
k1 = int(input('Digite a classe (k): '))
print(coef_binomial(n1, k1))
         
      
