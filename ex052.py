#Exercício Python 052: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
print('Analise de numeros \n  NUMEROS PRIMOS')
print('-='*10)
entrada = int(input('Digite um numero: '))
verificador = 0

for c in range(1, entrada+1):

    if entrada % c == 0:
        print('\033[31m{}\033[m'.format(c), end= ' ')
        verificador += 1
    else:
        print('\033[34m{}\033[m'.format(c), end=' ')

print('\n O numero {} foi divisil {} vezes ' .format(entrada, verificador))

if verificador == 2:
    print('Ele é um numero PRIMO')
else:
    print('Ele NÃO é um numero PRIMO')