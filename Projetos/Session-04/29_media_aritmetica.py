"""

Problem: Leia quatro notas, calcule a media aritmetica e imprima o resultado
Author: João Lucas
Pycamp

"""

print('======= Media aritmetica =======')

nota_1 = int(input('Digite a primeira nota \n'))

nota_2 = int(input('Digite a segunda nota \n'))

nota_3 = int(input('Digite a terceira nota \n'))

nota_4 = int(input('Digite a quarta nota \n'))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print('Sua media é {0}'.format(media))
