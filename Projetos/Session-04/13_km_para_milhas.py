"""

Problem: Leia uma distância em km e apresenta-a convertida em milhas.
        A fórmula de conversão é:
            M = K / 1.61
        Sendo K a distância em km e M em Milhas
Author: João Lucas
Pycamp

"""

print('======= Milhas para Km  =======')

k = float(input('Digite a distância em Km \n'))

m = round(k / 1.61, 2)

print('{0} km é igual a {1} milhas'.format(k, m))
