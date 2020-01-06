"""

Problem: Leia um valor de área em metros quadrados e apresente-o convertido em acres.
        A formula de conversão é:
            A = M * 0.000247
        Sendo M a area em metros quadrados e A a area em acres
Author: João Lucas
Pycamp

"""

print('======= Metros Quadrados para Acres =======')

m = float(input('Qual o valor em Metros Quadrados \n'))

a = m * 0.000247

print('{0} metros quadrados é igual a {1} acres'.format(m, a))
