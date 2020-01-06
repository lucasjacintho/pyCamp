"""

Problem: Leia um valor de massa em quilogramas e apresente-o convertido em libras
        A formula de conversão é:
            L = K / 0.45
        Sendo K a massa em quilogramas e L a massa em Libras
Author: João Lucas
Pycamp

"""

print('======= Quilogramas para Libras =======')

k = float(input('Digite o peso em kg \n'))

l = round(k / 0.45, 2)

print('{0} kg é igual a {1} libras'.format(k, l))
