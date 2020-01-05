"""

Problem: Leia uma distância em milhas e apresenta-a convertida em quilômetros.
        A fórmula de conversão é:
            K = 1.61 * M
        Sendo K a distância em km e M em Milhas
Author: João Lucas
Pycamp

"""

print('======= Milhas para Km  =======')

m = float(input('Digite a distância em Milhas \n'))

k = round(1.61 * m, 2)

print('{0} milhas é igual a {1} km/h'.format(m, k))
