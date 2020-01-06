"""

Problem: Leia um valor de volume em litros e apresente-o em metros cúbicos
        A formula de conversão é:
            M = L / 1000
        Sendo L o volume em litros e M o volume em metros cúbicos
Author: João Lucas
Pycamp

"""

print('======= Metros cúbicos em Litros =======')

litros = float(input('Digite o valor do volume em Litros \n'))

m = round(litros / 1000)

print('{0} em litros é igual a {1} metros cúbicos'.format(litros, m))
