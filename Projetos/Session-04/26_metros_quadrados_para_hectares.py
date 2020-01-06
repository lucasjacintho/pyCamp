"""

Problem: Leia um valor de area em metros quadrados e apresente-o convertido em hectares.
        A formula de conversão é:
            H = M * 0.0001
        Sendo M a area em metros quadrados e H a area em hectares
Author: João Lucas
Pycamp

"""

print('======= Metros Quadrados para Hectares =======')

m = float(input('Digite um valor em metros quadrados \n'))

h = m * 0.0001

print('{0} metros quadrados para {1} hectares'.format(m, h))
