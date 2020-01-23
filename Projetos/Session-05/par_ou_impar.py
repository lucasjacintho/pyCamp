"""

Problem: Faça um programa que receba um número inteiro e verifique se este número é par ou impar
Author: João Lucas
Pycamp

"""

print('======= Impar ou Par =======')

num = int(input('Digite um valor \n'))

if num % 2 == 0:
    print('O valor digitado {0} é par'.format(num))
else:
    print('O valor digitado {0} é impar'.format(num))


