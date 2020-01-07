"""

Problem: Leia a altura de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular.
        culculado por meio da seguinte formula:
            V = PI * raio ** 2 * altura
        Onde PI = 3.141592
Author: João Lucas
Pycamp

"""

print('======= Cilindro Circular =======')

pi = 3.141592

altura_cilindro = float(input('Qual a altura do cilindro \n'))

raio_cilindro = float(input('Qual o raio do cilindro \n'))

volume_cilindro = pi * ((raio_cilindro ** 2) * altura_cilindro)

print('O volume é igual a {0}'.format(volume_cilindro))
