"""

Problem: A nota final de um estudante é calculado a partir de tres notas atribuidas entre o intervalo
        de 0 até 10, respectivamente, a um trabalho de laboratorio, a uma avaliação semestral
        e a um exame final. A media das tres notas mencionadas anteriormente obedece aos pesos
        Trabalho de Laboratorio: 2
        Avaliação Semestral: 3
        Exame Final: 5
        De acordo com o resultado, mostre na tela se o aluno está reprovado (media entre 0 e 2.9)
        de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessarias
Author: João Lucas
Pycamp

"""

print('======= Media das Notas =======')

nota_lab = int(input("Qual a nota no trabalho de Laboratorio \n"))

nota_avaliacao = int(input("Qual a nota da avaliação \n"))

nota_exame = int(input("Qual a nota do exame final \n"))

if nota_lab < 0 and nota_lab > 10 and nota_avaliacao < 0 and nota_avaliacao > 10 and nota_exame < 0 and nota_exame > 10:
    print("As notas digitadas estão incorretas")
    print("Lembre-se que as notas devem estar entre 0 e 10")
else:
    media = (nota_lab * 2) + (nota_avaliacao * 3) + (nota_exame * 5) / 10
    if media <= 2.9:
        print("Aluno reprovado")
    elif media <= 4.9:
        print("Aluno em recuperação")
    else:
        print("Aluno aprovado")
