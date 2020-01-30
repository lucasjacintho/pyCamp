"""

Problem: Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem "Numero invalido".
        Se i numero for positivo, calcular o logaritmo deste numero
Author: João Lucas
Pycamp

"""

import math

print('======= Logaritmos =======')

num = int(input('Digite um valor \n'))

if num < 0:
    print("Numero invalido")
else:
    log_calc = math.log10(num)
    print("O logaritmo de {0} é igual a {1}".format(num, log_calc))
