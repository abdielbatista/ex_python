#declaração da função
def calc():
    t = 0
    num = 1
    den = 200
    #estrutura de repetição
    while num <= 100:
        f = num / den
        t = t + f
        num = num + 1
        den = den - 2

    return t

print (calc())