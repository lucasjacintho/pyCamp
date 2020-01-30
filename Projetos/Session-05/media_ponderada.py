"""

Problem: Faça um algoritmo que calcule a media ponderada das notas de 3 provas
        A primeira tem peso 2, a segunda peso 3 e a terceira tem peso 5. Ao final,
        mostrar a media do aluno
        e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
        superior a 60 pontos
Author: João Lucas
Pycamp

"""

print('======= Media Pondera =======')

prova_um = int(input("Digite o valor da primeira prova \n"))

prova_dois = int(input("Digite o valor da segunda prova \n"))

prova_tres = int(input("Digite o valor da terceira prova \n"))

media_ponderada = ((prova_um * 2) + (prova_dois * 3) + (prova_tres * 5))

if media_ponderada >= 60:
    print("Aluno aprovado")
elif media_ponderada < 60:
    print("Aluno reprovado")
else:
    print("Numeros digitados estão incorretos")
