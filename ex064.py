'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999,
  que é a condição de parada. No final, mostre quantos números foram digitados
  e qual foi a soma entre eles (desconsiderando o flag).'''

soma = 0
contador = 0
valor = 0
while valor !=999:
    valor = int(input('Digite um numero [999 para parar]: '))
    if valor != 999:
        soma += valor
        contador += 1
print(f'Você digitou {contador} números e a soma deles é {soma}.')