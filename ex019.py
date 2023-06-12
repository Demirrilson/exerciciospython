print('Escolhe o nome de um aluno aleatoriamente\n')
import random
a = input('1º aluno: ')
b = input('2º aluno: ')
c = input('3º aluno: ')
d = input('4º aluno: ')

e = random.choice([a, b, c, d])

print('O aluno escolhido foi: {}!' .format(e))
