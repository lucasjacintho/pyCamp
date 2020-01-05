"""

Problem: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin
        A formula de conversão é:
            K = C + 273.15
        Sendo C a temperatura em Celsius e K a temperatura em Kelvin
Author: João Lucas
Pycamp

"""

print('======= Celsius para Kelvin  =======')

c = float(input('Digite a temperatura em celsius \n'))

k = round(c + 273.15, 2)

print('O valor {0} em celsius é igual a {1} kelvin'.format(c, k))
