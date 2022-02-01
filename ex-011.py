'''Faça uma função capaz de gerar e retornar um vetor de n elementos aleatórios, 
composto por zeros e uns com probabilidades iguais de aparecerem no vetor. 
Sua função deve ter o seguinte protótipo def geraVetor ( n )'''

import random 

def geraVetor(n):

    
    i = 0
    v = []

    while(i <= n-1):

        x = random.randint(1, 100)
        
        if x <= 50:
            v.append(1)
        else:
            v.append(0)

        i = i + 1
    
    return v


def cruzamento(v1, v2):
    vetor = []
    n = len(v1)
    p = random.randint(0, (n - 1))

    for i in range (0, n):
        if(i <= (p - 1)):
            vetor.append(v1[i])
        else:
            vetor.append(v2[i])

    return vetor

vetor1 = geraVetor(5)
vetor2 = geraVetor(5)

f = cruzamento(vetor1, vetor2)

print(vetor1)
print(vetor2)
print(f)

