"""

Problem: Leia um valor de volume em metros cúbicos e apresente-o em litros
        A formula de conversão é:
            L = 1000 * M
        Sendo L o volume em litros e M o volume em metros cúbicos
Author: João Lucas
Pycamp

"""

print('======= Metros cúbicos em Litros =======')

m = float(input('Valor do metro cúbico \n'))

litros = round(1000 * m, 2)

print('{0} metros cúbicos e igual a {1} litros'.format(m, litros))
