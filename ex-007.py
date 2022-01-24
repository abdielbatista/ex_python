'''Faça uma função capaz de gerar um vetor de 10 elementos 
composto de zeros e uns, de modo que os zeros e uns tenham 
a mesma probabilidade de aparecerem no vetor.'''

import random 

def vetor():

    
    i = 0
    v = []

    while(i <= 10):

        n = random.randint(1, 100)
        
        if n <= 50:
            v.append('0')
        else:
            v.append('1')

        i = i + 1
    
    for i in range(10):
        print(v[i]) 
    

vetor()