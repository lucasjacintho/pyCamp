"""

Problem: Faça um programa que receba dois números e mostre qual deles é o maior
Author: João Lucas
Pycamp

"""

print('======= Maior Número =======')

num_1 = int(input('Digite o primeiro valor \n'))

num_2 = int(input('Digite o segundo valor \n'))

if num_1 > num_2:
    print("O primeiro valor é maior")
elif num_1 < num_2:
    print("O segundo valor digitado é maior")
else:
    print("Os dois valores digitados são iguais")
