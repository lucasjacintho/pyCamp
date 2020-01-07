"""

Problem: Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
Author: João Lucas
Pycamp

"""

print('======= Antecessor e o Sucessor =======')

a = int(input('Digite um número \n'))

antecessor = a * 2 - 1

sucessor = a * 3 + 1

res = antecessor + sucessor

print('O resultado é igual a {0}'.format(res))
