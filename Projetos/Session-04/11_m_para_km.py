"""

Problem: Leia uma velocidade em m/s e apresente-a convertida em km/h.
        A formula de conversão é:
        K = M * 3.6
        Sendo K a velocidade em km/h e M em m/s
Author: João Lucas
Pycamp

"""

print('======= m/s para km/h  =======')

m = float(input('Digite a velocidade em metros por segundo \n'))

k = round(m * 3.6, 2)

print('{0} m/s é igual a {1} km/h'.format(m, k))
