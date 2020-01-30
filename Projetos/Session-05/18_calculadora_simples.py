"""

Problem: Faça um programa que mostre ao usuario um menu com 4 opções de operações matematicas
        (as basicas, por exemplo). O usuario escolhe uma das opções e o seu programa então
        pede dois valores numericos e realiza a operação, mostrando o resultado e saindo
Author: João Lucas
Pycamp

"""

print('======= Calculadora Simples =======')

print("=============================================\n")
print("======= Escolha um dos Itens abaixo ======= \n")
print("1 - Soma")
print("2 - Multiplicação")
print("3 - Divisão")
print("4 - Subtração")
print("=============================================")

menu = int(input())

if menu > 0 and menu < 5:
    num_um = float(input("Digite um primeiro numero \n"))

    num_dois = float(input("Digite um segundo numero \n"))

    res = 0

    if menu == 1:
        res = num_um + num_dois
        pass
    elif menu == 2:
        res = num_um * num_dois
        pass
    elif menu == 3:
        res = num_um / num_dois
        pass
    elif menu == 4:
        res = num_um - num_dois
        pass

    print("Resultado: ", res)
















