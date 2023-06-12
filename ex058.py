'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar,
  mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

print('Sou o Computador...')
print('Acabei de pensar em um numero de 0 a 10.')
print('Tente adivinhar...')
computador = randint(0, 10)
jogador = int(input('Qual o seu palpite? '))
tentativas = 1
while computador != jogador:
    tentativas += 1
    if computador > jogador:
        print('Mais... Tente outra vez!')
    else:
        print('Menos... Tente outra vez!')
    jogador = int(input('Qual o seu palpite? '))
print('Acertou com {} tentativas. PaRaBenS!!!'.format(tentativas))
