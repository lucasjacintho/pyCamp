"""

Problem: Leia um valor de area em hectares e apresente-o convertido em metros quadrados.
        A formula de conversão é:
            M = H * 10000
        Sendo M a area em metros quadrados e H a area em hectares
Author: João Lucas
Pycamp

"""

print('======= Hectares para Metros Quadrados =======')

h = float(input('Qual o valor em hectares? \n'))

m = h * 10000

print('{0} hectares é igual a {1} metros quadrados'.format(h, m))
