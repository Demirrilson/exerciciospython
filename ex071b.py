'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('~~'*15)
print('===BANCO BRANCO===')
print('~~'*15)
saque = int(input('Qual o valor a sacar? R$'))
print('         ===SAQUE===')
total = saque
nota = 50
total_nota = 0

while True:
    if total >= nota:
        total -= nota
        total_nota += 1
    else:
        if total_nota > 0:
            print(f'Total de {total_nota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
            total_nota = 0
        elif nota ==20:
            nota = 10
            total_nota = 0
        elif nota == 10:
            nota = 1
            total_nota = 0
        if total == 0:
            break
