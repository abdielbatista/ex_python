'''Modifique a função do exercício anterior de modo que 
os números uns tenham 70% de probabilidade de aparecerem 
e os números zeros tenham 30% de probabilidade de aparecerem no vetor.'''

import random 

def vetor():

    
    i = 0
    v = []

    while(i <= 9):

        n = random.randint(1, 100)
        
        if n <= 70:
            v.append('1')
        else:
            v.append('0')

        i = i + 1
    
    for i in range(10):
        print(v[i]) 
    

vetor()