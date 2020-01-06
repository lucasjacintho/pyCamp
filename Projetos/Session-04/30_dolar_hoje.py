"""

Problem: Leia um valor em Real e a cotação do Dólar. Em seguida, imprima o valor correspondente em dólares
Author: João Lucas
Pycamp

"""

print('======= Dolar Hoje =======')

moeda_real = float(input('Quanto você tem em R$ \n'))

cotacao = float(input('Qual a cotação do Dólar? \n'))

convertido = round(moeda_real / cotacao, 2)

print('O valor R${0} convertido em dolares é igual a ${1}'.format(moeda_real, convertido))
