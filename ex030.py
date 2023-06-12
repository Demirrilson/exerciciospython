#Exercício Python 030: Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

x = int(input('\033[1;33mDigite um nomero: \033[m'))
y = x%2
if y==0:
    print('\033[4;36mO numero\033[m {} {} {} \033[32m é PAR '.format('\033[31m', x, '\033[m'))
else:
    print('O numero \033[35m{}\033[m é \033[31;7mIMPAR\033[m'.format(x))