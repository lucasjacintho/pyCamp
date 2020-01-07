"""

Problem: Leia um número inteiro e imprima o seu antecessor e o seu sucessor
Author: João Lucas
Pycamp

"""

print('======= Antecessor e o Sucessor =======')

a = int(input('Digite um número \n'))

print('O antecessor de {0} é: {1}'.format(a, a-1))

print('O sucessor de {0} é: {1}'.format(a, a+1))
