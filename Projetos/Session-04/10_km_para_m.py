"""

Problem: Leia uma velocidade em km/h e apresente-a convertida em m/s.
        A formula de conversão é:
        M = K/3.6
        Sendo K a velocidade em km/h e M em m/s
Author: João Lucas
Pycamp

"""

print('======= Km para m  =======')

k = float(input('Digite a velocidade em km/h \n'))

m = round(k / 3.6, 2)

print('{0} km/h é igual a {1} em m/s'.format(k, m))
