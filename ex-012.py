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

def getArray():
    vetor = []
    for i in range(1, 50):
        vetor.append(geraVetor(10))

    print(vetor)

getArray()