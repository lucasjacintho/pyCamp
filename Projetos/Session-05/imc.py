"""

Problem: Faç um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal
        utilizando as seguintes formulas:
            Homens: (72.7 * H) - 58
            Mulheres: (62.1 * H) - 44.7
        Onde H corresponde a altura
Author: João Lucas
Pycamp

"""

print('======= IMC =======')

altura = float(input('Qual a sua altura? \n'))

print('H = homem || M = mulher')

sexo = input('Qual o seu sexo \n')

imc = 0
if sexo == 'H':
    imc = (72.7 * altura) - 58
    print('Seu peso ideal é {0}'.format(imc))
elif sexo == 'M':
    imc = (62.1 * altura) - 44.7
    print('Seu peso ideal é {0}'.format(imc))
else:
    print('Por favor, o valor correto em sexo')
    print('Lembre-se: H = homem || M = mulher')
