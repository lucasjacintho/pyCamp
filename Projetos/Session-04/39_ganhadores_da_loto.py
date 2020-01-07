"""

Problem: A importancia de R$ 780.000,00 será dividia entre três ganhadores de um concurso.
        Sendo que da quantia total:
            O primeiro ganhador recebera 46%
            O segundo receberá 32%
            O terceiro receberá o restante
Author: João Lucas
Pycamp

"""

print('======= Ganhadores da loto =======')

valor_premio = 780000

primeiro_lugar = valor_premio * 0.46

segundo_lugar = valor_premio * 0.32

terceiro_lugar = valor_premio - (primeiro_lugar + segundo_lugar)

print('O primeiro lugar ganhou: ', primeiro_lugar)

print('O segundo lugar ganhou: ', segundo_lugar)

print('O terceiro lugar ganhou: ', terceiro_lugar)