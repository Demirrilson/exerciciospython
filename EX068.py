'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint
computador = jogador = contador = 0
teste = ''
print('~~'*20)
print('===JOGO DE PAR OU IMPAR===')
print('~~'*20)
while True:
    print('***' * 15)
    computador = randint(0,10)
    jogador = int(input('Diga um valor: '))

    #while teste not in 'pi':
    teste = str(input('Par ou Impar? [P/I] ')).strip().lower()

    soma = computador + jogador

    if soma % 2 ==0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR')
    elif soma % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu IMPAR')

    if teste == 'p' and soma % 2 == 0:
        print('Você VENCEU!!!')
        print('***' * 15)
        print('Vamos jogar novamnete...')
    elif teste == 'p' and soma % 2 != 0:
        print('Você PERDEU!!!')
        break

    if teste == 'i' and soma % 2 != 0:
        print('Você VENCEU!!!')
        print('***' * 15)
        print('Vamos jogar novamnete...')
    elif teste == 'i' and soma % 2 == 0:
        print('Você PERDEU!!!')
        break

    contador += 1

print('***'*15)
print(f'GAME OVER!!! VOCÊ VENCEU {contador} VEZES.')
