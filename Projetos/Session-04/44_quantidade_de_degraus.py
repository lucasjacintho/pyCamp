"""

Problem: Receba a altura do degrau de uma escada e a altura que o usuario deseja alcançar subindo a escada.
        Calcule e mostre quantos degraus o usuario deverá subir para atingir seu objetivo
Author: João Lucas
Pycamp

"""

print('======= Quantidade de Degraus =======')

altura_degrau = float(input('Qual a altura do degrau \n'))

objetivo_altura = float(input('Qual altura você deseja alcançar \n'))

objetivo_final = round(objetivo_altura / altura_degrau)

print('Você deve subir um total de {0} degraus para atingir seu objetivo'.format(objetivo_final))
