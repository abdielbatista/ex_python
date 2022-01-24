'''Faça um programa em C++ que receba como entrada a nota de um aluno 
entre 0 e 100 e faça o seguinte:
• se a nota for inválida (não estiver entre 0 e 100), 
apresentará uma mensagem informandoo caso;
• se a nota do aluno for maior ou igual a 60 apresentará a mensagem “APTO”;
• senão apresentará a mensagem “EM CONSTRUÇÃO”.'''

#declaração da função
def calc(nota):
    #estrutura de verificação 
    if nota > 100 or nota < 0:
        return ("NOTA INVALIDA")
    elif nota >= 60:
        return ("APTO")
    else:
        return ("EM CONSTRUÇÃO")

#nota recebe o valor informado pelo usuario
nota = float(input("Digite a nota do aluno: "))

#result chama a funçaõ e repassa o valor para o calculo
result = calc(nota)

print(result)