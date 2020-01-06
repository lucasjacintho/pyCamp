"""

Problem: Leia um valor de área em acres e apresente-o convertido em metros quadrados.
        A formula de conversão é:
            M = A * 4048.58
        Sendo M a area em metros quadrados e A a area em acres
Author: João Lucas
Pycamp

"""

print('======= Acres para Metros Quadrados =======')

a = float(input('Digite o valor do Acre \n'))

m = a * 4048.58

print('{0} acre é igual a {1} metros quadrados'.format(a, m))
