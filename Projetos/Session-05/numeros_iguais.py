"""

Problem: Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois numeros forem
        iguais, imprima a mensagem "Numeros iguais"
Author: João Lucas
Pycamp

"""

print('======= Numeros Iguais =======')

num_um = int(input('Digite um primeiro valor \n'))

num_dois = int(input('Digite um segundo valor \n'))

if num_um == num_dois:
    print('Os dois números são iguais')
elif num_um > num_dois:
    print('O maior valor é {0}'.format(num_um))
else:
    print('O maior valor é {0}'.format(num_dois))
