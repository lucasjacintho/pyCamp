"""

Problem: Leia um valor de comprimento em metros e apresente-o convertido em jardas.
        A formula de conversão é:
            J = M / 0.91
        Sendo J o comprimento em jardas e M o comprimento em metros
Author: João Lucas
Pycamp

"""

print('======= Metros para Jarda =======')

m = float(input('Digite o comprimento em metros \n'))

j = round(m / 0.91, 2)

print('{0} metros é igual a {1} jardas'.format(m, j))
