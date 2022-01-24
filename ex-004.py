'''Faça um programa em que faça exatamente o contrário da questão anterior, 
ou seja: o usuário deve informar a quantidade de horas, minutos e segundos, 
e o programa fará a conversão do valor digitado para segundos. 
Assim, se o usuário digitar os valores 21, 55 e 15,
o programa dará como saída 78915 segundos.'''

#declaração da função
def horaCalc(h, m, s):
    #conversão da hora para segundos
    hora = h*3600;
    #conversão dos minutos para segundos
    min = m*60;
    
    #a função retorna a soma de hora, minutos e segundos, 
    #todos ja convertidos para segundos
    return hora + min + s

#usuario entra com os dados
h = int(input("Digite a hora: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

#hora chama a função para realizar o calculo
hora = horaCalc(h, m, s)

print(hora, "segundos")
