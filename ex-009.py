'''Modifique a função do exercício anterior de modo que 
os números uns tenham 70% de probabilidade de aparecerem 
e os números zeros tenham 30% de probabilidade de aparecerem no vetor.'''

import random 

def vetor():

    i = 0
    v = []
    contUm = 0
    contZero = 0

    while(i <= 999):

        n = random.randint(1, 100)
        
        if n <= 70:
            v.append(int(1))
        else:
            v.append(int(0))

        i = i + 1
    
    for i in range(1000):
        if v[i] == 1:
            contUm = contUm + 1
        else:
            contZero = contZero + 1

            
    
    print(contUm / 1000)
    print('')
    print(contZero / 1000)
    

vetor()