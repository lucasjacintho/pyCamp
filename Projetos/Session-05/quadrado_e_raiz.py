"""

Problem: Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
        - O número digitado ao quadrado
        - A raiz quadrada do número digitado
Author: João Lucas
Pycamp

"""

print('======= Raiz Quadrada =======')

num = int(input('Digite um valor \n'))

if num < 0:
    print('O valor é invalido')
else:
    num_square = num ** 2
    num_raiz = num ** 0.5
    print('O valor de {0} ao quadrado é igual a {1} \n'.format(num, num_square))
    print('O valor da raiz quadrada de {0} é igual a {1}'.format(num, num_raiz))

