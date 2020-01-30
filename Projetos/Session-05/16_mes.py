"""

Problem: Usando SWITCH, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mes
        correspondente a este numero. Isto é, Janeiro se for 1, Fevereiro se for 2
        e assim por diante
Author: João Lucas
Pycamp

"""

print('======= Meses =======')

num = int(input("Digite um numero entre 1 e 12 \n"))

if num == 1:
    print("Janeiro")
    pass
elif num == 2:
    print("Fevereiro")
    pass
elif num == 3:
    print("Março")
    pass
elif num == 4:
    print("Abril")
    pass
elif num == 5:
    print("Maio")
    pass
elif num == 6:
    print("Junho")
    pass
elif num == 7:
    print("Julho")
    pass
elif num == 8:
    print("Agosto")
    pass
elif num == 9:
    print("Setembro")
    pass
elif num == 10:
    print("Outubro")
    pass
elif num == 11:
    print("Novembro")
    pass
elif num == 12:
    print("Dezembro")
    pass
else:
    print("Numero digitado não esta entre 1 e 12")