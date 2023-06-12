'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total_compra = 0
mais_de_mil = 0
menor_preco = 0
menor_preco_nome = ''
contador = 0

while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    total_compra += preco

    if preco > 1000:
        mais_de_mil += 1
    contador += 1
    if contador == 1:
        menor_preco = preco
        menor_preco_nome = produto
    if preco < menor_preco:
        menor_preco = preco
        menor_preco_nome = produto
    teste = ''
    while teste != 's' and teste != 'n':
        teste = str(input('Quer continuar? [S/N] '))
    if teste =='n':
        break
print('~~'*20)
print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor_preco_nome} que custa R${menor_preco:.2f}')