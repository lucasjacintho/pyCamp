"""

Problem: Leia um ângulo em graus e apresente-o convertido em radianos.
        A formula de conversão é:
            R = G * PI /180
        Sendo G o ângulo em graus e R em radianos e PI 3.14
Author: João Lucas
Pycamp

"""

print('======= Grau em Radiano  =======')

g = float(input('Digite o valor do ângulo \n'))

r = round((g * 3.14) / 180, 2)

print('O ângulo {0} é igual a {1} em radiano'.format(g, r))
