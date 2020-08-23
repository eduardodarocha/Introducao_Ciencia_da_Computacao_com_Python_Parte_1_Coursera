# somador de algarismos
soma = 0
num = int(input('Digite um número inteiro: '))
while num != 0:
    alg = num % 10
    num = num // 10
    soma = soma + alg
print(soma)      
