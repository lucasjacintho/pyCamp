"""

Problem: Escreva um programa que dado dois numeros inteiros mostre na tela o maior
        deles assim como a diferença existente entre ambos
Author: João Lucas
Pycamp

"""

print('======= Numeros inteiros =======')

num_um = int(input('Digite um primeiro valor \n'))

num_dois = int(input('Digite um segundo valor \n'))

num_diff = 0

if (num_um > num_dois):
    num_diff = num_um - num_dois
    print('O {0} é o maior valor'.format(num_um))
    print('A diferença entre eles é igual a {0}'.format(num_diff))
else:
    num_diff = num_dois - num_um
    print('O {0} é o maior valor'.format(num_dois))
    print('A diferença entre eles é igual a {0}'.format(num_diff))

