'''Usando apenas duas variáveis inteiras, 
faça um programa em que solicite ao usuário que
digite 5 números. Ao final, o programa escreverá na tela 
o produto de todos os números digitados.'''

#declaração da função
def multi (n1, n2):
    #operação matematica
    return n1 * n2


p = 1

#usuario insere os valores
n = int(input("Digite um número "))
#e p recebe o return da função de operação
p = multi(p, n)


n = int(input("Digite um número "))
p = multi(p, n)

n = int(input("Digite um número "))
p = multi(p, n)

n = int(input("Digite um número "))
p = multi(p, n)

n = int(input("Digite um número "))
p = multi(p, n)

n = int(input("Digite um número "))
p = multi(p, n)

#mostra o resultado na tela
print(p)
