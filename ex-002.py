'''Faça um programa que solicite ao usuário que digite 
os valores de dois pontos (A e B) em um plano cartesiano 
(cada ponto é representado por suas coordenadas x e y). O
programa dará como saída a distância entre os dois pontos digitados.'''

import math

def distancia (xa, xb, ya, yb):
    d = ((xb - xa)**2) + ((yb - ya)**2)

    raiz = math.sqrt(d)
    
    return raiz

xa = int(input("Digite o valor Xa: "))
xb = int(input("Digite o valor Xb: "))
ya = int(input("Digite o valor Ya: "))
yb = int(input("Digite o valor Yb: "))

r = int(distancia(xa, xb, ya, yb))

print(r)