"""

Recebendo dados do usuario


input() -> Todo tipo recebido via input é do tipo String

"""

# Entrada de Dados
print("Qual o seu nome?")
nome = input()

idade = int(input('Qual a sua idade?'))

# Processamento

# Saída de dados

# Formato de print do 2.x
# print('Seja bem-vindo(a) %s' % nome)
# print('O %s tem %s anos' % (nome, idade))

# Versão moderna de print 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))
# print('O {0} tem {1} anos'.format(nome, idade))

# Versão mais usada apartir da versão 3.7
# print(f'Seja bem-vindo(a) {nome}')
# print(f'O {nome} tem {idade} anos')
