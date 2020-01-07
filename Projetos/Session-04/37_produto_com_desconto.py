"""

Problem: Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
Author: João Lucas
Pycamp

"""

print('======= Produto com desconto =======')

produto_valor = float(input('Qual o valor do produto \n'))

valor_final = produto_valor - (produto_valor * 0.12)

print('Valor anterior: {0} \nnovo valor: {1}'.format(produto_valor, valor_final))
