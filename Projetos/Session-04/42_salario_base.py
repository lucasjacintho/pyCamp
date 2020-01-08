"""

Problem: Receba o salario-base de um funcionario. Calcule e imprima o salario a receber, sabendo-se que esse funcionario
        tem uma gratificação de 5% sobre o salario-base. Além disso ele paga 7% de imposto sobre o salario-base
Author: João Lucas
Pycamp

"""

print('======= Salario-Base =======')

salario_base = float(input('Qual o salario-base do funcionario \n'))

gratificacao = salario_base * 0.05

imposto = salario_base * 0.07

salario_pagar = (salario_base + gratificacao) - imposto

print('Salario a receber: ', salario_pagar)
