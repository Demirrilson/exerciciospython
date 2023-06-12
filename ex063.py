'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
 e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. '''
print('Sequência de FIBONACCI')
print('=*='*9)
fim = int(input('Quantos termos vc quer mostras?'))
anterior =0
proximo = 0
contador = 2

termo1 = 0
termo2 = 1
termox = 1
print(f'{termo1} → {termo2} → ', end='')
while contador < fim:
    termox += anterior
    proximo = anterior + termox
    anterior = termox -anterior
    contador += 1
    print(f'{termox} → ', end='')
print('FIM')