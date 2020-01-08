"""

Problem: Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
Author: João Lucas
Pycamp

"""

print('======= Ano de Nascimento =======')

ano_atual = int(input('Qual o ano atual \n'))

idade_atual = int(input('Qual a sua idade \n'))

dt_nascimento = ano_atual - idade_atual

print('Você nasceu em ', dt_nascimento)
