"""

Problem: Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999)
        Gere outro número formado pelos digitos invertidos do numero lido
Author: João Lucas
Pycamp

"""

print('======= Número invertido =======')

numero = input('Digite um número entre 100 - 999 \n')

if(numero >= '100' and numero <= '999'):
    print(str(numero)[::-1])
else:
    print('Por favor! Digite um numero Válido')