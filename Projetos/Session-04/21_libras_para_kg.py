"""

Problem: Leia um valor de massa em libras e apresente-o convertido em kg
        A formula de conversão é:
            K = L * 0.45
        Sendo K a massa em quilogramas e L a massa em Libras
Author: João Lucas
Pycamp

"""

print('======= Libras para KG =======')

l = float(input('Digite o peso em libras \n'))

k = round(l * 0.45, 2)

print('{0} libras é igual a {1} kg'.format(l, k))
