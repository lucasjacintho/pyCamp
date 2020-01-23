"""

Problem: Faça um programa que receba dois números e mostre qual deles é o maior
Author: João Lucas
Pycamp

"""

print('======= Raiz Quadrada =======')

num = int(input('Digite um valor \n'))

if num >= 0:
    num_raiz = num ** 0.5
    print('A raiz quadrado de {0} é igual a {1}'.format(num, num_raiz))
else:
    print('Número digitado é invalido')
