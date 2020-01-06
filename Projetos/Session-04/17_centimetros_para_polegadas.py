"""

Problem: Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas
        A formula de conversão é:
            P = C / 2.54
        Sendo C o comprimento em centimetros e P o comprimento em polegadas
Author: João Lucas
Pycamp

"""

print('======= Centimetros em Polegadas =======')

c = float(input('Qual o valor em centimetros? \n'))

p = round(c / 2.54, 2)

print('O valor {0} em centimetros e igual a {1} polegadas'.format(c, p))
