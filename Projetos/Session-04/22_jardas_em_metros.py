"""

Problem: Leia um valor de comprimento em jardas e apresente-o convertido em metros.
        A formula de conversão é:
            M = 0.91 * J
        Sendo J o comprimento em jardas e M o comprimento em metros
Author: João Lucas
Pycamp

"""

print('======= Jardas para Metros =======')

j = float(input('Digite o comprimento em Jardas \n'))

m = round(0.91 * j, 2)

print('{0} jardas é igual a {1} metros'.format(j, m))
