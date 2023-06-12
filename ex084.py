'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
registro = []
dados = []
total_pessoas = maior_peso = menor_peso = 0
contador = 0
continua = ''
nome_peso_menor = []
nome_peso_maior = []
dados.append(str(input('Nome: ')))
dados.append(float(input('Peso: ')))
registro.append(dados[:])
dados.clear()

while True:
    continua = str(input('Quer continuar? [S/N]')).upper().strip()
    if continua == 'N':
        break
    elif continua != 'S':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()
    else:
        dados.append(str(input('Nome: ')))
        dados.append(float(input('Peso: ')))
        registro.append(dados[:])
        dados.clear()

for reg in registro:
    if contador == 0:
        maior_peso = reg[1]
        menor_peso = reg[1]
    elif contador > 0:
        if reg[1] > maior_peso:
            maior_peso = reg[1]
        elif reg[1] < menor_peso:
            menor_peso = reg[1]
    contador += 1

print(f'Foram  cadastradas {contador} pessoas.')
print(f'O maior peso foi de {maior_peso}KG. Peso de {nome_peso_maior}')
print(f'O menor peso foi de {menor_peso}KG. Peso de {nome_peso_menor}')
print(registro)