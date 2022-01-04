'''Faça um programa que solicite ao usuário um número inteiro 
que representa uma quantidade de segundos. 
O programa exibirá na tela o valor convertido em horas, minutos e
segundos. Assim, se o usuário digitar o valor 78915, 
o programa dará como saída 21 horas, 55 min e 15 segundos.'''


import time

h = int(input("Digite um numero: "))

hora = time.strftime("%H horas %M minutos e %S segundos", time.gmtime(h))

print (hora)

