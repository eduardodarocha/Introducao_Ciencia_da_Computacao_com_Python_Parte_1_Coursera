num = int(input('Digite um número inteiro: '))
alg1 = num % 10
while num > 0:
    num = num // 10
    alg2 = num % 10
    if alg1 == alg2:
        print('sim')
        break
    else:
        if num > 0:
            alg1 = alg2
        else:
            break
if num == 0:
    print('não')
