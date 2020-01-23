"""

Problem: Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela
        a media destas notas. Uma nota valida deve ser, obrigatoriamente um valor entre 0.0 e 10.0, onde
        caso a nota não possua um valor valido, este fato deve ser informado ao usuario e o programa termina.
Author: João Lucas
Pycamp

"""

print('======= Notas do Aluno =======')

nota_um = float(input('Digite a primeira nota do aluno \n'))

nota_dois = float(input('Digite a segunda nota do aluno \n'))

if (nota_um >= 0 and nota_um <= 10 and nota_dois >= 0 and nota_dois <= 10):
    media = (nota_um + nota_dois)/2
    print('A media do aluno é {0}'.format(media))
else:
    print('As notas não são validas')