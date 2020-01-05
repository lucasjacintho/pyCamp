"""

Problem: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius
        A formula de conversão é:
            C = 5.0 * (F - 32.0)/9.0
        Sendo C a temperatura em Celsius e F a temperatura em Fahrenheit
Author: João Lucas
Pycamp

"""

print('======= Farenheit para Celsius =======')

f = float(input('Digite a temperatura em Fahrenheit \n'))

c = round(5.0 * (f - 32.0)/9.0, 1)

print('O valor {0} em farenheit é igual a {1} celsius'.format(f, c))
