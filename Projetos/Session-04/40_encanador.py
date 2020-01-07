"""

Problem: Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias
        trabalhadors pelo encanador e imprima a quantia líquida que deverá ser paga.
        Sabendo-se que são descontados 8% para imposto de renda
Author: João Lucas
Pycamp

"""

print('======= Encanador =======')

valor_dia = 30

dias_encanador = int(input('Qual o total de dias trabalhados \n'))

valor_bruto = valor_dia * dias_encanador

valor_liquido = valor_bruto * 0.8

print('Valor bruto: ', valor_bruto)
print('Valor liquido: ', valor_liquido)

