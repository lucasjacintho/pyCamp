"""

Problem: Usando SWITCH, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
        da semana correspondente a este numero. Isto é, domingo se for 1, segunda-feira se for 2
        e assim por diante
Author: João Lucas
Pycamp

"""

print('======= Dias da Semana =======')

num = int(input("Digite um numero entre 1 e 7 \n"))

if num == 1:
    print("Domingo")
    pass
elif num == 2:
    print("Segunda-Feira")
    pass
elif num == 3:
    print("Terça-Feira")
    pass
elif num == 4:
    print("Quarta-Feira")
    pass
elif num == 5:
    print("Quinta-Feira")
    pass
elif num == 6:
    print("Sexta-Feira")
    pass
elif num == 7:
    print("Sabado")
    pass
else:
    print("Numero digitado não esta entre 1 e 7")