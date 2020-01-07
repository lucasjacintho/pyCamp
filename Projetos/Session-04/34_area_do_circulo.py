"""

Problem: Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente
        Formula de calculo é
            PI * raio ** 2
        Sendo PI = 3.141592
Author: João Lucas
Pycamp

"""

print('======= Areá do Circulo =======')

raio_circulo = float(input('Qual o valor do raio \n'))

area_circulo = 3.141592 * (raio_circulo ** 2)

print('A área do circulo é igual a: {0}'.format(area_circulo))
