"""

Problem: Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês
        Imprima o valor a ser pago ao funcionario, adicionando 10% sobre o valor calculado
Author: João Lucas
Pycamp

"""

print('======= Aumento Salarial =======')

valor_hora = float(input('Qual o valor da hora desse funcionario \n'))

numero_hora_mes = float(input('Qual foi o total de horas trabalhadas \n'))

salario_mes = valor_hora * numero_hora_mes

valor_final = salario_mes + (salario_mes * 0.1)

print('Total a ser Pago: ', valor_final)
