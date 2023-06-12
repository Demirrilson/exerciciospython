# jogo da adivinhação!
import random
print('Vou pensar em um numero inteiro entre 0 e 5')
numero = int(input('Em qual numero eu pensei? '))
x = random.choice([0,1,2,3,4,5])
print('PROCESSANDO...')
from time import  sleep
sleep(1)
if numero == x:
    print('Você GANHOU !')
else:
    print('Eu ganhei! pensei no numero {} e você digitou {}' .format(x, numero))
print('==fim==')