# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

print('-=' * 20)
print(str('        Conversão de BASE '))
print('=-' * 20)
numero = int(input('Digite um numero inteiro: '))
print('Digite: \n[1] = binario \n[2] = octal \n[3] = hexadecimal')
base = int(input('BASE: '))

if base == 1:
    print('O numero {} em binario é: \033[1;32m{}\033[m'.format(numero, (bin(numero)[2:])))
elif base == 2:
    print('O numero {} em octal é: \033[1;32m{}\033[m'.format(numero, (oct(numero)[2:])))
elif base == 3:
    print('O numero {} em Hexadecimal é: \033[1;32m{}\033[m'.format(numero, (hex(numero)[2:])))
else:
    print('\033[1;31m{}\033[m Não correspode a uma Opção Valida'.format(base))
