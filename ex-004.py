'''Faça um programa em que faça exatamente o contrário da questão anterior, 
ou seja: o usuário deve informar a quantidade de horas, minutos e segundos, 
e o programa fará a conversão do valor digitado para segundos. 
Assim, se o usuário digitar os valores 21, 55 e 15,
o programa dará como saída 78915 segundos.'''


def horaCalc(h, m, s):
    hora = h*3600;
    min = m*60;
    
    return hora + min + s;


h = int(input("Digite a hora: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

hora = horaCalc(h, m, s)

print(hora, "segundos")
