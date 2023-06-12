'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
maior = []
menor = []
posicao_maior = []
posicao_menor = []
for l in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {l}: ')))
print(f'Você digitou os valores {lista}')

for cont in range (0,5):
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    elif cont > 0:
        if maior < lista[cont]:
            maior = lista[cont]
        elif lista[cont] < menor:
            menor = lista[cont]

print(f'O Maior valor digitado foi {maior} nas posições: ', end='')
for c, v in enumerate(lista):
    if maior == v:
        posicao_maior.append(c)
        print(f'{c}', end='...')
print(f'\nO Menor valor digitado foi {menor} nas posições: ', end='')
for c, v in enumerate(lista):
    if menor == v:
        posicao_menor.append(c)
        print(f'{c}', end='...')






