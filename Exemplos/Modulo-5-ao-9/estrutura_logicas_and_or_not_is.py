"""

Estruturas logicas: AND (e), OR (ou), NOT (não), IS (e)

Operadores Unarios
    - NOT
Operadores Binarios
    - AND, OR, IS

"""

ativo = True
logado = True


# 01

if ativo and logado:
    print('Bem-vindo usuario')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# 02

if ativo or logado:
    print('Bem-vindo usuario')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# 03

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuario')

# 04
print(ativo is False)