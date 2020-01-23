"""

Problem: Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado
Author: João Lucas
Pycamp

"""

print('======= Raiz Quadrada =======')

num = int(input('Digite um valor \n'))

if num >= 0:
    num_raiz = num ** 0.5
    print('A raiz quadrado de {0} é igual a {1}'.format(num, num_raiz))
else:
    num_square = num ** 2
    print('Você digitou um valor negativo, logo será apresentado o quadrado do mesmo e não sua raiz \n')
    print('O quadrado de {0} é igual a -{1}'.format(num, num_square))
