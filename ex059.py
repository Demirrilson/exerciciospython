'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep

variavel1 = float(input('Digite um valor: '))
variavel2 = float(input('Digite outro valor: '))
opcao = 0

while opcao != 5:

    print('==-=='*4)
    print('[1] somar\n[2] multiplicar \n[3]maior \n[4]novos números \n[5] sair do programa')
    opcao = int(input('>>>>Qual a sua opção? '))
    print('==-=='*4)

    if opcao == 1:
       soma = variavel2 + variavel1
       print( 'O resultado de {} + {} = {}'.format(variavel1, variavel2, soma))

    elif opcao == 2:
        multiplicar = variavel1 * variavel2
        print('O resultado de {} x {} = {}' .format(variavel1, variavel2, multiplicar))

    elif opcao == 3:
        if variavel1 > variavel2:
            print('Entre {} e {} o maior valor é {}'.format(variavel1, variavel2, variavel1))
        elif variavel2 > variavel1:
            print('Entre {} e {} o maior valor é {}'.format(variavel1, variavel2, variavel2))
        else:
            print('São iguais')

    elif opcao == 4:
        variavel1 = float(input('Digite um valor: '))
        variavel2 = float(input('Digite outro valor: '))

    elif opcao == 5:
        print(' Saindo do programa ...')

    else:
        print('Opção invalida... Tente novamente!')
    sleep(2)

print('Volte sempre!!')
