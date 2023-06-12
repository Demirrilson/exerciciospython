'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

notas50 = notas20 = notas10 = notas1 = 0
print('~~'*15)
print('===BANCO BRANCO===')
print('~~'*15)
saque = int(input('Qual o valor a sacar? R$'))

while True:
    notas50 = saque //50
    sobra =  saque % 50
    notas20 = sobra //20
    sobra = sobra % 20
    notas10 =sobra // 10
    sobra = sobra % 10
    notas1 =  sobra // 1
    sobra =  sobra % 1
    if sobra == 0:
        break
print('         ===SAQUE===')
if notas50 >0:
    print( f'Total de {notas50:.0f} cédulas de R$50')
if notas20 >0:
    print( f'Total de {notas20:.0f} cédulas de R$20')
if notas10 >0:
    print( f'Total de {notas10:.0f} cédulas de R$10')
if notas1 >0:
    print( f'Total de {notas1:.0f} cédulas de R$1')
