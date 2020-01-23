"""

Problem: Leia o salario de um trabalhador e o valor da prestação de um emprestimo. Se a prestação for maior
        que 20% do salario imprima "Emprestimo não concedido", caso contario imprima "Emprestimo concedido"
Author: João Lucas
Pycamp

"""

print('======= Emprestimos =======')

sal = float(input('Qual o salario? \n'))

valor_emp = float(input('Qual o valor do emprestimo? \n'))


if (valor_emp >= (sal * 0.2)):
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')
