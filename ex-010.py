'''Faça uma função capaz de gerar e retornar um vetor de n elementos aleatórios, 
composto por zeros e uns com probabilidades iguais de aparecerem no vetor. 
Sua função deve ter o seguinte protótipo def geraVetor ( n )'''

import random 

def vetor(n):

    
    i = 0
    v = []

    while(i <= n-1):

        x = random.randint(1, 100)
        
        if x <= 50:
            v.append('1')
        else:
            v.append('0')

        i = i + 1
    
    for i in range(n):
        print(v[i]) 
    

n = 10

vetor(n)
