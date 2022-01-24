'''Faça um programa que solicite ao usuário que digite 
os valores de dois pontos (A e B) em um plano cartesiano 
(cada ponto é representado por suas coordenadas x e y). O
programa dará como saída a distância entre os dois pontos digitados.'''

#importação da biblioteca
import math

#declaração da função
def distancia (xa, xb, ya, yb):
    #operação ultilizando a formula para o calculo
    d = ((xb - xa)**2) + ((yb - ya)**2)

    #raiz recebe a raiz quadrada do resultado armazenado em d
    #a raiz quadrada é calculada pela função sqrt acessada da biblioteca math
    raiz = math.sqrt(d)
    
    return raiz

#usuario entra com os dados
xa = int(input("Digite o valor Xa: "))
xb = int(input("Digite o valor Xb: "))
ya = int(input("Digite o valor Ya: "))
yb = int(input("Digite o valor Yb: "))

#r recebe o return da função
r = int(distancia(xa, xb, ya, yb))

print(r)