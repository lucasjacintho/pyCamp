"""

Problem: Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
            O total a pagar com desconto de 10%
            O valor de cada parcela, no parcelamento de 3x sem juros
            A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
            A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
Author: João Lucas
Pycamp

"""

print('======= Ajudando Vendedores =======')

valor_produto = float(input('Qual o valor do Produto \n'))

valor_desconto = valor_produto - (valor_produto * 0.1)

valor_parcelado = round(valor_produto / 3, 2)

comissao_a_vista = valor_desconto * 0.05

comissao_parcelada = valor_produto * 0.05

print('Total a pagar com desconto de 10% - R$', valor_desconto)

print('Valor da parcela 3x sem juros - R$', valor_parcelado)

print('Comissão do vendedor na venda a vista - R$', comissao_a_vista)

print('Comissão do vendedos na venda parcelada - R$', comissao_parcelada)
