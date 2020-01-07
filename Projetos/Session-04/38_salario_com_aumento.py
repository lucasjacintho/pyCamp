"""

Problem: Leia o salário de um funcionario. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%
Author: João Lucas
Pycamp

"""

print('======= Aumento de Salario =======')

salario = float(input('Qual o salario do funcionario \n'))

novo_salario = salario + (salario * 0.25)

print('Antigo salario: {0}\nNovo salario: {1}'.format(salario, novo_salario))
