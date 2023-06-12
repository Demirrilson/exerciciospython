'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

soma = media = maior = menor = contator = 0
teste = 's'

while teste != 'n':
    if teste == 's':
        valor = int(input('Digite um numero: '))
        contator += 1
        if contator == 1:
            maior = valor
            menor = valor
        elif contator > 1:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor
    teste = str(input('Você quer continuar? [S/N]: ')).lower().strip()[0]
    soma += valor

media = soma / contator

print(f'A média entre os valores é {media}.')
print(f'o maior numero digitado foi {maior} e o menor foi {menor}.')
print(f'Você digitou {contator} numeros.')

