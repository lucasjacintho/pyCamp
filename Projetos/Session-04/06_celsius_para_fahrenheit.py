"""

Problem: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit
        A formula de conversão é:
            F = C * (9.0/5.0) + 32.0
        Sendo F a temperatura em Fahrenheit e C a temperatura em Celsius
Author: João Lucas
Pycamp

"""

print('======= Celsius para Farenheit =======')

c = float(input('Digite a temperatura em graus Celsius \n'))

f = round(c * (9.0 / 5.0) + 32.0, 1)

print('O {0} celsius é igual a {1} farenheit'.format(c, f))
