"""

Problem: Faça um programa que calcule e mostre a area de um trapezio. Sabe-se que
        A = ((baseMaior + baseMenor) * altura) / 2
Author: João Lucas
Pycamp

"""

print('======= Area de um trapezio =======')

base_maior = float(input("Qual o valor da Base Maior \n"))

base_menor = float(input("Qual o valor da Base Menor \n"))

altura = float(input("Qual a Altura desse trapezio \n"))

if base_maior > 0 and base_menor > 0:
    trapezio = ((base_menor + base_maior) * altura) / 2
    print("Area do trapezio é igual a", trapezio)
else:
    print("Bases devem ser maior que 0")

