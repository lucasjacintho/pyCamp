"""

Problem: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius
        A formula de conversão é:
            C = K - 273.15
        Sendo C a temperatura em Celsius e K a temperatura em Kelvin
Author: João Lucas
Pycamp

"""

print('======= Kelvin para Celsius =======')

k = float(input('Digite o valor em Kelvin \n'))

c = round(k - 273.15, 2)

print('O valor {0} kelvin e igual a {1} celsius'.format(k, c))
