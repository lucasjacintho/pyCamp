"""

Problem: Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
Author: João Lucas
Pycamp

"""

print('======= Segundos para Horas e Minutos =======')

numero_segundos = int(input('Qual o valor em segundos \n'))

valor_horas = numero_segundos / 3600

valor_minutos = numero_segundos / 60

print(valor_horas)
print(valor_minutos)

