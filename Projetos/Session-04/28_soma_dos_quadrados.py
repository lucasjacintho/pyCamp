"""

Problem: Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos
Author: João Lucas
Pycamp

"""

print('======= Somando os quadrados =======')

valor_a = int(input('Digite o primeiro valor \n'))

valor_b = int(input('Digite o segundo valor \n'))

valor_c = int(input('Digite o terceiro valor \n'))

res = (valor_a ** 2) + (valor_b ** 2) + (valor_c ** 2)

print('A soma dos quadrados {0}, {1}, {2} é igual a {3}'.format(valor_a, valor_b, valor_c, res))
