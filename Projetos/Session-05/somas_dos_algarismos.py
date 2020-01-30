"""

Problem: Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela a soma de todos
        os seus algarismos. Por exemplo, ao numero 251 correspondera o valor 8 (2+5+1). Se o numero lido não
        for maior do que zero, o programa terminara com a mensagem "Numero invalido"
Author: João Lucas
Pycamp

"""

print('======= Somando os Algorismos =======')

num = input("Digite um numero inteiro \n")


"""

    ____ $Função nova
    A função nativa sum calcula a soma dos itens de um objeto iterável. 
    Por padrão, a função input retorna uma string, que é iterável no Python. 
    Como queremos a soma algébrica dos dígitos, 
    basta converter cada um para o tipo inteiro.

"""
print(sum(int(i) for i in num))
