"""

Problem: Leia um ângulo em radiano e apresente-o convertido em grau.
        A formula de conversão é:
            G = R * 180 / PI
        Sendo G o ângulo em graus e R em radianos e PI 3.14
Author: João Lucas
Pycamp

"""

print('======= Radiano em Grau =======')

r = float(input('Digite o valor de um radiano \n'))

g = round(r * (180 / 3.14), 2)

print('{0} radiano é igual a {1} grau'.format(r, g))
