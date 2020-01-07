"""

Problem: Sejam A e B os catetos de um triangulo, onde a hipotenusa é obtida pela equação:
            hipotenusa = √A**2 + B**2
        Faça um programa que receba os valores de A e B e calcule o valor da hipotenusa através da equação.
        Imprima o resultado dessa opeção
Author: João Lucas
Pycamp

"""
import math

print('======= Catetos e Hipotenusa =======')

a = float(input('Qual o valor do lado A \n'))

b = float(input('Qual o valor do lado B \n'))

hipotenusa = math.hypot(a, b)

print(hipotenusa)
