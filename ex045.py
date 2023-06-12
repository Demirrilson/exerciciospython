#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']

print('Vamos jogar JOKENPÔ')
print('-='*15)
print('ESTAS SÃO AS OPÇÃO: \n [0] para PEDRA \n [1] para PAPEL \n [2] para TESOURA')

opcao_jogador = int(input('Digite sua opção: '))
opcao_computador = randint(0,2)
print('-='*15)
print('====JO====')
sleep(1)
print('====KEN====')
sleep(1)
print('====PÔ====')
sleep(1)
print('-='*15)
print('Você jogou {} \nO computador jogou {}' .format(itens[opcao_jogador], itens[opcao_computador]))
print('-='*15)

if opcao_computador == 0:
    if opcao_jogador == 0:
        print('EMPATE!!')
    elif opcao_jogador == 1:
        print('VOCÊ GANHOU!!!')
    elif opcao_jogador == 2:
        print('O COMPUTADOR GANHOU!!!')
elif opcao_computador ==1:
    if opcao_jogador ==0:
        print('O COMPUTADOR GANHOU!!!')
    elif opcao_jogador == 1:
        print('EMPATE!!')
    elif opcao_jogador == 2:
        print('VOCÊ GANHOU!!!')
elif opcao_computador ==2:
    if opcao_jogador == 0:
        print('VOCÊ GANHOU!!!')
    elif opcao_jogador == 1:
        print('O COMPUTADOR GANHOU!!!')
    elif opcao_jogador == 2:
        print('EMPATE!!')
else:
    print('OPÇÃO INVALIDA')