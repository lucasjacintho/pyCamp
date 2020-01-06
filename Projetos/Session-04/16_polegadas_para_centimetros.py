"""

Problem: Leia um valor de comprimentoi em polegadas e apresente-o convertido em centimetros
        A formula de conversão é:
            C = P * 2.54
        Sendo C o comprimento em centimetros e P o comprimento em polegadas
Author: João Lucas
Pycamp

"""

print('======= Polegadas em Centimetros =======')

p = float(input('Qual o valor em polegadas? \n'))

c = round(p * 2.54, 2)

print('O valor {0} e igual a {1} em centimetros'.format(p, c))


