#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso_maoir = 0
peso_menor = 0

for c in range(1,6):

    pessoa = float(input('Qual o peso da {}ª pessoa? ' .format(c)))
    if c == 1:
        peso_maior = pessoa
        peso_menor = pessoa
    else:
        if pessoa > peso_maoir:
            peso_maoir = pessoa
        if pessoa < peso_menor:
            peso_menor = pessoa

print('O maior peso foi {}KG '.format(peso_maoir))
print('O menor peso foi {}KG '.format(peso_menor))