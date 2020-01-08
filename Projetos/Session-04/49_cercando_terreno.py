"""

Problem: Faça um programa para ler as dimensões de um terreno (C comprimento e L Largura)
        Bem como o preço do metro de tela P. Imprima o custo para cercar este mesmo terreno com tela
Author: João Lucas
Pycamp

"""

print('======= Cercando terreno =======')

comprimento_terreno = float(input('Qual o comprimento desse terreno \n'))
largura_terreno = float(input('Qual a largura desse terreno \n'))
preco_tela = float(input('Qual o preço do metro de tela \n'))

tamanho_area = comprimento_terreno * largura_terreno

valor_final = tamanho_area * preco_tela

print('Você pagara R${0} para cercar {1}m²'.format(valor_final, tamanho_area))